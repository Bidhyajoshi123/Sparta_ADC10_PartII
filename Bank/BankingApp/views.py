from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Customer
from django.db.models import Q
from django.core.files.storage import FileSystemStorage 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def add_new(request):
    if request.method == "POST":
        temp = Customer()
        temp.firstname = request.POST['firstname']
        temp.lastname = request.POST['lastname']
        temp.account_no = request.POST['account_no']
        temp.contact_no = request.POST['contact_no']
        temp.save()
        return redirect(index)
    else:
        return render(request, "add_new.html")

def show_all(request):
    if Customer.objects.count() > 0:
        data = Customer.objects.all()
        return render(request, "show-all.html", {'data':data})
    else: 
        return render(request, "show-all.html")

def edit_delete(request):
    if Customer.objects.count() > 0:
        data = Customer.objects.all()
        return render(request, "edit-delete.html",{'data':data})
    else: 
         return render(request, "edit-delete.html") 

def delete(request, id):   
    temp = Customer.objects.get(id=id)
    temp.delete()
    return redirect(edit_delete)

def edit(request, id):
    if request.method =="POST":
        temp = Customer.objects.get(id=id)
        temp.firstname = request.POST['firstname']
        temp.lastname = request.POST['lastname']
        temp.account_no = request.POST['account_no']
        temp.contact_no = request.POST['contact_no']
        temp.save()
        return redirect(edit_delete)
    else: 
        temp = Customer.objects.get(id=id)
        return render(request,"edit.html", {'temp': temp})    


def search(request):
    srch = request.GET.get('srh')
    if srch :
        match = Customer.objects.filter(Q(firstname__icontains=srch))
        return render(request,'show-all.html', {'data':match})
    return render(request,'search.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html',context)

def signup(request):
    if request.method == "GET":
        return render(request,'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful!!!")