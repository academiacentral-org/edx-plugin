"""
Lawrence McDaniel - https://lawrencemcdaniel.com
Feb-2022

Scaffolding for future use.
"""
from django.conf.urls import url
from .views.gradebook_api import spoc_gradebook

# this repo
app_name = "openedx_plugin"

urlpatterns = [
    url(r"^gradebook/?$", spoc_gradebook, name="spoc_gradebook"),
] 