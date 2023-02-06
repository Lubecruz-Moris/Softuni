from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_departments(request, *args, **kwargs):
    body = f"Args = {args}, Kwargs = {kwargs}"
    return HttpResponse(body)