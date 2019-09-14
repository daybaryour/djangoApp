#Serializer.py enables the rest APu to convert python responses in JSON 

from rest_framework import serializers
from applicants.models import Applicants

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = '__all__'