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

    if bool(firstname) or bool(lastname) or bool(job):
        #applicants = Applicants.objects.raw("SELECT * FROM applicants_applicants WHERE firstname LIKE %'" +firstname+ "'% OR '"+lastname+ "' LIKE %'" +lastname +"'% OR job LIKE %'" + job + "'%")
        results = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM applicants_applicants WHERE firstname LIKE '%"+firstname+"%' OR lastname LIKE '%"+lastname+"%' OR job LIKE '%"+job+"%'")

            for obj in cursor.fetchall():
                results.append({"id": obj[0], "firstname": obj[1], "lastname": obj[2] , "age": obj[3], "job": obj[4], "created": obj[5]})
        applicants = results

        #applicants = Applicants.objects.raw("SELECT * FROM applicants_applicants WHERE firstname LIKE '%ade%' OR lastname LIKE '%ojugbeli%' OR job LIKE '%harm%' OR age LIKE '' OR created_at LIKE '' ")
    else:
        applicants = Applicants.objects.all()

    return render(request, 'index.html', {'applicants': applicants}) #passing 

def add_applicant(request):
    return render(request, 'add_applicant.html')

def filter_applicants(request):
    filtered_results = Applicants.objects.raw('SELECT * FROM applicants_applicants WHERE firstname LIKE %firstname% AND lastname LIKE %lastname% AND job LIKE %job%')
    pprint(filtered_results)