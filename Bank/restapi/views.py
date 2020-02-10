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




