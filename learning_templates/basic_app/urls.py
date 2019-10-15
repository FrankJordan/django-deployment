from django.conf.urls import url
from django.urls import path, include
from basic_app import views

# This is needed for Template Tagging

app_name = "basic_app"

urlpatterns = [
    path("relative/", views.relative, name="relative"),
    path("other/", views.other, name="other"),

]
