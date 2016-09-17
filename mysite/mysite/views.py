from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import mysql.connector

def index(request):
    return render(request, 'index.html')


def model(request):
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='fintech')
    cursor = cnx.cursor(dictionary=True)
    model_id = request.GET.get('id', '1')
    query = "SELECT * FROM fintech.model_stocks WHERE model_id=%s"
    cursor.execute(query, model)
    stock_list =[]
    for stock in cursor:
        stock_list.append(stock)
    cursor.close()
    cnx.close()
    context = {'stock_list': stock_list}
    return render(request, 'ModelDetail.html',context)

