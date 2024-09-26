from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from .filters import JobFilter

from . import models
# Create your views here.
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required

def job_list(request):
    job_list = models.Job.objects.all()
    # filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs
    
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {"jobs":page_obj,'tot_job':job_list,'myfilter':myfilter}
    return render(request,"job/job_list.html",context)


def job_detail(request, slug):
    job_detail = models.Job.objects.get(slug=slug)
    if request.method == 'POST' :
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    context = {"job":job_detail, 'form':form}
    return render(request,"job/job_details.html",context)

@login_required
def add_job(request):
    if request.method == 'POST' :
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    context = {'form':form}
    
    return render(request,"job/add_job.html",context)

