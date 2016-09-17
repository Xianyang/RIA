from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
# Create your views here.
from django.http import JsonResponse
def model_list(request):
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='fintech')
    cursor = cnx.cursor(dictionary=True)
    query = ("SELECT * FROM fintech.models")
    cursor.execute(query)
    model_list = []
    for model in cursor:
        model_list.append(model)
    cursor.close()
    cnx.close()
    return JsonResponse({'model_list':model_list})


def index(request):
    return HttpResponse("")
