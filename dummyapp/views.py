from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import DonorForm, RobinForm, LoginRobin, LoginDonor, CreateFoodForm, AuthForm
from django.contrib import messages
import requests
import json
import base64
import cv2
import sys

user = 'admin'
pwd = 'getRektm8@'
headers = {"Content-Type":"application/json","Accept":"application/json"}
donors = {}
robins = {}
foods = {}
donors_id = robins_id = foods_id = {}

def faq(request):
    return render(request, 'FAQ.html')

def askq(request):
    return render(request, 'AskQuestion.html')

def home(request):
    return render(request, 'Homepage.html')

def index_donor(request):
    form = {}
    return render(request, 'index_donor.html', {'form': form})

def index_robin(request):
    form = {}
    return render(request, 'index_robin.html', {'form': form})

def get_donors():
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors?sysparm_limit=10'
    response = requests.get(url, auth=(user, pwd), headers=headers)
    data = response.json()
    data_result = data['result']
    #print(data)
    return data_result



def get_robins():
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_robins?sysparm_limit=10'
    response = requests.get(url, auth=(user, pwd), headers=headers)
    data = response.json()
    data_result = data['result']
    result = {}
    print(data_result)
    return result



def get_foods():
    url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_food?sysparm_limit=10'
    response = requests.get(url, auth=(user, pwd), headers=headers)
    data = response.json()
    data_result = data['result']
    for i in data_result:
        foods_id[i['number']] = i['sys_id']
    return data_result


def login_donor(request):
    donors = get_robins()
    if request.method == 'POST':
        form = LoginDonor(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd1']

    form = LoginDonor()
    return render(request, 'login_donor.html', {'form':form})

def login_robin(request):
    donors = get_robins()
    if request.method == 'POST':
        form = LoginRobin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['pwd1']

    form = LoginRobin()
    return render(request, 'login_robin.html', {'form':form})

def register_robin(request):
    if request.method == 'POST':
        form = RobinForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            designation = form.cleaned_data['designation']
            email = form.cleaned_data['email']
            transport = form.cleaned_data['transport']
            contact = form.cleaned_data['contact']

            url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_robins'
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            data = {"name": name, "location": location, "contact": contact, "email":email, "designation":designation, "contact":contact}
            data = json.dumps(data, separators=(',', ':'))
            response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
            data = response.json()

    form = RobinForm()
    return render(request, 'form_robin.html', {'form': form})

def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            pwd1 = form.cleaned_data['pwd1']

            url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_donors'
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            data = {"name": name, "location": location, "contact": contact, "pwd1":pwd1, "email":email}
            data = json.dumps(data, separators=(',', ':'))
            response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
            data = response.json()

    form = DonorForm()
    return render(request, 'form_donor.html', {'form': form})

def create_food_record(request):
    if request.method == 'POST':
        form = CreateFoodForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            status = 1
            url = 'https://dev64891.service-now.com/api/now/table/x_263107_robinarmy_food'
            data = {"donor_name":name,"quantity":quantity,"type":type,"status":status, "location":location}
            data = json.dumps(data, separators=(',', ':'))
            response = requests.post(url, auth=(user, pwd), headers=headers, data=data)
            data = response.json()
    form = CreateFoodForm()
    return render(request, 'form_food.html', {'form': form})

def robin_dashboard(request):
    food = get_foods()
    return render(request, 'robin_dashboard.html', {'food':food})


def calculate_points(request):
    robins = get_robins()
    return render(request, 'robin_dashboard.html', {'food':food})


def robin_delivering(request):
    food = get_foods()
    del food[0]
    return render(request, 'robin_delivering.html', {'food':food})

def anon_donate(request):
    food = get_foods()


def authenticate(request):
    if request.method == 'POST':
        form = AuthForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.cleaned_data['image']
            #cv2.imshow("Faces found", 'abba.png')
            n = detect_faces(img)
            return redirect('success.html')
    form = AuthForm()
    return render(request, 'authenticate.html', {'form': form})

def detect_faces(img):
    # Get user supplied values
    imagePath = 'abba.png'
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    imagePath = str(imagePath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, gray, COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))
    return len(faces)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)

def robin_delivering(request):
    return render(request, 'robin_delivering.html')
