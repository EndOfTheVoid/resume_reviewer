from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_files, name='upload_files'),
    path("multiple_upload", views.multiple_upload, name='multiple_upload'),
    path("description", views.description, name="description"),
    path("results", views.results, name="results"),

]