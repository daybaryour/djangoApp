#api.py file will handle the endpoints availability (No auth was implemented here)

from applicants.models import Applicants
from rest_framework import viewsets, permissions
from applicants.serializers import ApplicantSerializer

#Applicant Viewset create CRUD without specifying all the methods explicitly
class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicants.objects.all()
    permissions = [
        permissions.AllowAny
    ]

    serializer_class = ApplicantSerializer

        
    