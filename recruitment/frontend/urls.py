from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_applicant', views.add_applicant),
]

