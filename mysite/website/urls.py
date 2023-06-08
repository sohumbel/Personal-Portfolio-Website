from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path("projects/",views.project_index, name = "project_index")
]