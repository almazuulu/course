import imp
from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

class CourseList(ListView):
    model = Course