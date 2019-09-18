from django.shortcuts import render
from django.db import connection
from applicants.models import Applicants
from pprint import pprint
import sys

# Create your views here.
def index(request):
    firstname = request.GET.get('firstname', False)
    lastname = request.GET.get('lastname', False)
    job = request.GET.get('job', False)

    applicants = Applicants.objects.all()

    if bool(firstname) or bool(lastname) or bool(job):
        if bool(firstname):
            applicants = applicants.filter(firstname__icontains=firstname)

        if bool(lastname):
            applicants = applicants.filter(lastname__icontains=lastname)

        if bool(job):
            applicants = applicants.filter(job__icontains=job)
        

    return render(request, 'index.html', {'applicants': applicants}) #passing 

def add_applicant(request):
    return render(request, 'add_applicant.html')

def filter_applicants(request):
    filtered_results = Applicants.objects.raw('SELECT * FROM applicants_applicants WHERE firstname LIKE %firstname% AND lastname LIKE %lastname% AND job LIKE %job%')
    pprint(filtered_results)