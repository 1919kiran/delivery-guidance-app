from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import DonorForm, RobinForm, LoginRobin, LoginDonor, CreateFoodForm
from django.contrib import messages
import requests
import json
import base64

user = 'admin'
pwd = 'getRektm8@'
headers = {"Content-Type":"application/json","Accept":"application/json"}
main_url = 'https://dev63955.service-now.com/api/now/'
donors_list = {}
robins_list = {}


def index_donor(request):
    form = {}
    return render(request, 'index.html', {'form': form})

def index_robin(request):
    form = {}
    return render(request, 'index.html', {'form': form})


# def get_donors(request):
#     url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_robins?sysparm_limit=1'
#     headers = {"Content-Type": "application/json", "Accept": "application/json"}
#     response = requests.get(url, auth=(user, pwd), headers=headers)
#     data = response.json()
#     print(data)
#     return render(request, 'index.html', {'data': data})
#
# def get_robins(request):
#     url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_robins?sysparm_limit=1'
#     headers = {"Content-Type": "application/json", "Accept": "application/json"}
#     response = requests.get(url, auth=(user, pwd), headers=headers)
#     data = response.json()
#     print(data)
#     return render(request, 'index.html', {'data': data})

def login_donor(request):
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors?sysparm_limit=10'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    data = response.json()
    data = data['result']
    print(data)

    if request.method == 'POST':
        messages.info(request, "You are now logged in.")
        form = LoginDonor(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd1 = form.cleaned_data['pwd1']
            messages.info(request, "You are now logged in.")
            return redirect('dummyapp:login_robin')
    form = LoginDonor()
    return render(request, 'form_login_donor.html', {'form': form})


def login_robin(request):
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors?sysparm_limit=10'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    data = response.json()
    data = data['result']
    print(data)

    if request.method == 'POST':
        form = LoginDonor(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd1 = form.cleaned_data['pwd1']
            messages.info(request, "You are now logged in.")
            return redirect('dummyapp:login_robin')
    form = LoginDonor()
    return render(request, 'form_login_donor.html', {'form': form})


def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            email = form.cleaned_data['email']
            pwd1 = form.cleaned_data['pwd1']
            location = form.cleaned_data['location']

            url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors'
            data = {"name":name,"contact":contact,"email":email,"pwd1":pwd1,"pwd2":pwd2,"location":location,}
            data = json.dumps(data, separators=(',', ':'))
            response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
            return redirect('dummyapp:login_donor')
            if response.status_code != 200:
                print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
                exit()
            data = response.json()
            print(data)
    else:
        form = DonorForm()
        return render(request, 'form_register_donor.html', {'form': form})

def register_robin(request):
    if request.method == 'POST':
        form = RobinForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            designation = form.cleaned_data['designation']
            email = form.cleaned_data['email']
            pwd1 = form.cleaned_data['pwd1']
            location = form.cleaned_data['location']
            transport = form.cleaned_data['transport']

            url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_robins'
            headers = {"Content-Type":"application/json","Accept":"application/json"}
            data = {"name":name,"contact":contact,"designation":designation,"email":email,"pwd1":pwd1,"location":location,"transport":transport}
            data = json.dumps(data, separators=(',', ':'))
            response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
            return redirect('dummpyapp:login_robin')
    form = DonorForm()
    return render(request, 'form_register_robin.html', {'form': form})


def create_food_record(request):
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_food'
    if request.method == 'POST':
        form = CreateFoodForm()
        img = form.food_img
        name = form.cleaned_data['name']
        quantity = form.cleaned_data['quantity']
        image_read = img.read()
        img_64 = base64.encodestring(image_read)
        img_64 = str(img_64)
        data = {"img_64": img_64, "name":name, "quantity":quantity}
        response = requests.post(url, auth=(user, pwd), headers=headers ,data="{\"dist_photo\":\"\",\"robin_name\":\"\",\"quantity\":\"\"}")

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            exit()

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        print(data)
    form = CreateFoodForm()
    return render(request, 'form_food.html', {'form': form})

# def register_donor(request):
#     if request.method == 'POST':
#         form = DonorForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             contact = form.cleaned_data['contact']
#             email = form.cleaned_data['email']
#             pwd1 = form.cleaned_data['pwd1']
#             pwd2 = form.cleaned_data['pwd2']
#             location = form.cleaned_data['location']
#
#             url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors'
#             headers = {"Content-Type":"application/json","Accept":"application/json"}
#             data = {"name":name,"contact":contact,"email":email,"pwd1":pwd1,"pwd2":pwd2,"location":location,}
#             data = json.dumps(data, separators=(',', ':'))
#             response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
#             if response.status_code != 200:
#                 #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
#                 exit()
#             data = response.json()
#             print(data)
#
#     form = DonorForm()
#     return render(request, 'form.html', {'form': form})
