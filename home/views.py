from pyexpat.errors import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser  # Import CustomUser model

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_number = request.POST['phone_number']  # Get phone number

        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'signup.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Phone number already registered.")
            return render(request, 'signup.html')

        # Create user
        user = CustomUser.objects.create_user(username=username, email=email, password=password1, phone_number=phone_number)
        user.save()

        # Log the user in and redirect to the home page
        login(request, user)
        return redirect('home')  # Replace 'home' with your actual home URL name
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')



def index(request):
    people = [
        {'name': 'Divya', 'age': 16},
        {'name': 'Divy', 'age': 20},
        {'name': 'Dia', 'age': 21},
        {'name': 'Diya', 'age': 16},
        {'name': 'Diya', 'age': 60},
    ]
    
    # Determine voting eligibility
    for person in people:
        person['can_vote'] = person['age'] >= 18
    
    return render(request, "index.html", context={'people': people})

def services(request):
    return render (request,"services.html")

def home(request):
    return render (request,"home.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render (request,"contact.html")

def index(request):
    return render(request, 'index.html')

def booking(request):
    return render(request, 'booking.html')  

def blog(request):
        return render(request, 'blog.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, id):
    blog = get_object_or_404(BlogPost, id=id)
    return render(request, 'home/blog_detail.html', {'blog': blog})

def process_booking(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date_time = request.POST.get('date_time')
        payment_method = request.POST.get('payment_method')

        # Process booking and payment details here

        # Return confirmation message
        return HttpResponse(f"Thank you {first_name} {last_name}, your booking for {service} on {date_time} has been received! Payment method: {payment_method}.")
    else:
        return redirect('booking')  # Redirect to booking form if accessed via GET

