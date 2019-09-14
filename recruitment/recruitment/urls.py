from django.contrib import admin #django admin here
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')), #includung all the urls for frontend url file
    path('', include('applicants.urls')), #includung all the urls for applicants url file
    #path('admin/', admin.site.urls),
]
