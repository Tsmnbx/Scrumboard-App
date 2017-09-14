from django.conf.urls import url

from .api import ListApi, CardApi


#Each is clling function url
#Url function maps url to a view
#First parameter is a regular expression which is iself a string
#Regular expression(from CSC240) reprsents other strings
#r means raw string ^ = begining to string trying to match
#$ matches the end of string I'm trying to match
#View Function

urlpatterns = [
    url(r'^list$', ListApi.as_view()),
    url(r'^cards$', CardApi.as_view())
]
