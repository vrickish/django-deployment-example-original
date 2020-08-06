from django.urls import path
from . import views

# Template Tagging

app_name = 'tempApp'

urlpatterns = [
    path("about/", views.about, name="about"),
    path("relative_url/", views.relative, name="relative"),
]
