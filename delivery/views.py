#from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from . models import Customer, Restaurant

# Create your views here.
def index(request):
    return render(request, 'index.html')

def open_signin(request):
    return render(request, 'signin.html')

def open_signup(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        # You would typically save the user to the database here
        #return render(request, 'signup_success.html', {'username': username})
        try:
            Customer.objects.get(username=username)
            return render(request, 'signup_fail.html')
        except:
            Customer.objects.create(username=username, password=password, email=email, mobile=mobile, address=address)
            return render(request, 'signin.html')
    
def signin(request):
    if request.method == 'POST':
        # Handle signin logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # You would typically verify the user credentials here
    try:
        Customer.objects.get(username=username, password=password)
        if(username=="pooja"):
            return render(request, 'admin_home.html')
        else:
            return render(request, 'customer_home.html')
    except Customer.DoesNotExist:
        return render(request, 'signin_fail.html')
    
def add_restaurant_page(request):
    return render(request,"add_restaurant_page.html")

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        # You would typically save the restaurant 
        Restaurant.objects.create(name=name, picture=picture, cuisine=cuisine, rating=rating)
        restaurants = Restaurant.objects.all()
        return render(request, 'show_restaurants.html' , {'restaurants': restaurants})
    return HttpResponse("Failed to add restaurant")

def open_show_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'show_restaurants.html', {"restaurants": restaurants})

