from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import mysql.connector
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')


def model(request,model_id):
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='fintech')
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM model_stocks WHERE model_id = %s" 
    cursor.execute(query, (model_id,))
    model_stock_list =[]
    for model_stock in cursor:
        model_stock_list.append(model_stock)

    id_str = [str(model_stock["stock_id"]) for model_stock in model_stock_list]
    id_str_param=', '.join(map(lambda x: '%s', id_str))
    query = "SELECT * FROM fintech.stocks WHERE id IN (%s)"
    query = query % id_str_param

    cursor.execute(query, id_str)

    stock_list =[]
    for stock in cursor:
        for model_stock in model_stock_list:
            if stock["id"] == model_stock["stock_id"]:
                stock["weight"] = model_stock["weighting"]
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

@csrf_exempt
def save_user_profile(request):
    request.session["user_age"] = request.POST['user_age']
    request.session["retire_age"] = request.POST["retire_age"]
    request.session["risk_preference"] = request.POST["risk_preference"]
    request.session["user_annual_saving"] = request.POST["user_annual_saving"]
    request.session["user_annual_withdraw"] = request.POST["user_annual_withdraw"]
    print(request.POST["user_annual_withdraw"])
    return HttpResponse("save user profile success")

def create_portfolio(request):
    model_id = "1"
    cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='fintech')
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM model_stocks WHERE model_id = %s"
    cursor.execute(query, (model_id,))
    model_stock_list =[]
    for model_stock in cursor:
        model_stock_list.append(model_stock)

    id_str = [str(model_stock["stock_id"]) for model_stock in model_stock_list]
    id_str_param=', '.join(map(lambda x: '%s', id_str))
    query = "SELECT * FROM fintech.stocks WHERE id IN (%s)"
    query = query % id_str_param
    cursor.execute(query, id_str)

    stock_list =[]
    for stock in cursor:
        for model_stock in model_stock_list:
            if stock["id"] == model_stock["stock_id"]:
                stock["weight"] = model_stock["weighting"]
                stock["units"] = int(100000 * stock["weight"] / stock["price"])
                stock["cost"] = 100000 * stock["weight"]
        stock_list.append(stock)
    query = "SELECT * FROM fintech.models WHERE id=%s"

    cursor.execute(query, (model_id,))
    model = {}
    for m in cursor:
        model = m

    cursor.close()
    cnx.close()
    context = {'stock_list': stock_list,"model":model}

    return render(request, 'user_portfolio.html',context)

def show_monte_carlo_result(request):
    return render(request, 'monte_carlo.html')



