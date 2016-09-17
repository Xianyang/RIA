from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

def index(reqeust):
    response = JsonResponse({'stock_list': [{"id":"123"},{}]})
    return response
