from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Customer


def customer_data(request):
    if request.method == "GET":
        customer = Customer.objects.all()
        dict = {
            "customers":list(customer.values("customer_firstname", "customer_lastname", "customer_account_no", "customer_contact_no"))
        }
        return JsonResponse(dict)

def get_customer(request, pk):
    if request.method == "GET":
        try:
            customer = Customer.objects.get(pk=pk)
            response = json.dumps([{'firstname':customer.customer_firstname, 'lastname':customer.customer_lastname, 'account_no': customer.customer_lastname, 'contact_no':customer.customer_contact_no}])
            return HttpResponse(response, content_type='text/json')
        except:
            return JsonResponse({"Error":"No customer with the given name found."})

@csrf_exempt
def update_api_data(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "PUT":
        json_data = request.body.decode('utf-8')
        update_data = json.loads(json_data)
        customer.customer_firstname = update_data['customer_firstname']
        customer.customer_lastname = update_data['customer_lastname']
        customer.customer_account_no = update_data['customer_account_no']
        customer.customer_contact_no = update_data['customer_contact_no']
        customer.save()
        return JsonResponse({"Success":"Customer Successfully Updated!!"})
    elif request.method == "DELETE":
        customer.delete()
        return JsonResponse({"Success":"Customer Successfully Deleted!!"})




