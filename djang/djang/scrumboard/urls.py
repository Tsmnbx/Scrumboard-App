from django.conf.urls import url
from django.views.generic import TemplateView

#from .api import ListApi, CardApi

from .api import ListViewSet, CardViewSet
from rest_framework.routers import DefaultRouter 


#Each is clling function url
#Url function maps url to a view
#First parameter is a regular expression which is iself a string
#Regular expression(from CSC240) reprsents other strings
#r means raw string ^ = begining to string trying to match
#$ matches the end of string I'm trying to match
#View Function

"""urlpatterns = [
    url(r'^list$', ListApi.as_view()),
    url(r'^cards$', CardApi.as_view()),
    url(r'^home', TemplateView.as_view(template_name = "scrumboard/home.html")),
]
"""
#genrates urls for these views
router = DefaultRouter()
router.register(r'lists',ListViewSet)
router.register(r'cards', CardViewSet)
# registars all url mapings with django
urlpatterns = router.urls