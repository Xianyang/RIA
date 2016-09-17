from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import mysql.connector

def index(request):
    return render(request, 'index.html')


def model(request,model_id):
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='fintech')
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM model_stocks WHERE model_id = %s" 
    cursor.execute(query, (model_id,))
    stock_list =[]
    for stock in cursor:
        stock_list.append(stock)
    query = "SELECT * FROM fintech.models WHERE id=%s"
    cursor.execute(query, (model_id,))
    model = {}
    for m in cursor:
        model = m
    
    cursor.close()
    cnx.close()
    context = {'stock_list': stock_list,"model":model}
    return render(request, 'ModelDetail.html',context)

