from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_number = request.POST['phone_number']

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

        user = CustomUser.objects.create_user(
            username=username, 
            email=email, 
            password=password1, 
            phone_number=phone_number
        )
        user.save()

        login(request, user)
        return redirect('home')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
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
    
    for person in people:
        person['can_vote'] = person['age'] >= 18
    
    return render(request, "index.html", context={'people': people})

def services(request):
    return render(request, "services.html")

def home(request):
    return render(request, "home.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")

def booking(request):
    return render(request, 'booking.html')

def blog(request):
    blogs = [
        {
            'id': 1,
            'title': 'The Art of Wedding Photography',
            'content': 'Wedding photography is an art that requires both technical skill and creative vision...',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST368j8vaV1uHWS-LGeH5mpcvIZ-Gp9FgaMA&s',
            'short_description': 'Explore the magic moments we capture in weddings...',
            'author': 'John Smith',
            'date': '2024-03-15'
        },
        {
            'id': 2,
            'title': 'Creative Pre-Wedding Shoot Ideas',
            'content': 'Pre-wedding photoshoots have become an essential part of the wedding journey...',
            'image_url': 'https://www.weddingreels.in/wp-content/uploads/2022/01/pre-wedding3.jpg',
            'short_description': 'Get inspired by unique themes for your pre-wedding photoshoot...',
            'author': 'Sarah Johnson',
            'date': '2024-03-14'
        },
        {
            'id': 3,
            'title': 'Post-Processing Tips for Flawless Photos',
            'content': 'Post-processing is a crucial step in creating stunning photographs...',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD8_Gv6_B6n7mlcDuBEZNUf96ELq2PsALihx8TwL7IPkesmBhpH95JZWL9NrsbHZXvlhg&usqp=CAU',
            'short_description': 'Learn professional editing tips to bring out the best in every shot...',
            'author': 'Mike Wilson',
            'date': '2024-03-13'
        }
    ]
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blogs = {
        1: {
            'title': 'The Art of Wedding Photography',
            'content': 'Wedding photography is an art that requires both technical skill and creative vision. A wedding photographer must capture not just images, but emotions, moments, and memories that will last a lifetime. From preparation shots in the morning to the final dance at night, each moment tells part of the couples unique story.\n \n Key aspects of wedding photography include:\n\n1. Preparation and Planning\n- Meeting with the couple beforehand\n- Understanding their vision and preferences\n- Scouting the venue for perfect shot locations\n\n2. Technical Excellence\n- Using appropriate equipment\n- Managing different lighting conditions\n- Capturing both posed and candid moments\n\n3. Storytelling Through Images\n- Creating a narrative flow\n- Capturing key moments and emotions\n- Documenting both big events and small details',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST368j8vaV1uHWS-LGeH5mpcvIZ-Gp9FgaMA&s',
            'author': 'John Smith',
            'date': '2024-03-15'
        },
        2: {
            'title': 'Creative Pre-Wedding Shoot Ideas',
            'content': 'Pre-wedding photoshoots have become an essential part of the wedding journey. They offer couples a chance to create beautiful memories before their big day. Here are some creative ideas for stunning pre-wedding photos:\n\n1. Location Selection\n- Natural landscapes\n- Urban settings\n- Meaningful places for the couple\n\n2. Theme Ideas\n- Vintage romance\n- Modern minimalist\n- Fantasy and fairytale\n- Travel and adventure\n\n3. Styling Tips\n- Coordinated outfits\n- Props and accessories\n- Natural poses and interactions\n\n4. Time of Day\n- Golden hour shots\n- Blue hour magic\n- Night photography',
            'image_url': 'https://www.weddingreels.in/wp-content/uploads/2022/01/pre-wedding3.jpg',
            'author': 'Sarah Johnson',
            'date': '2024-03-14'
        },
        3: {
            'title': 'Post-Processing Tips for Flawless Photos',
            'content': 'Post-processing is a crucial step in creating stunning photographs. Here are professional tips for enhancing your images:\n\n1. Basic Adjustments\n- Exposure correction\n- Color balance\n- Contrast enhancement\n\n2. Advanced Techniques\n- Skin retouching\n- Color grading\n- Background enhancement\n\n3. Consistency in Style\n- Developing a signature look\n- Batch processing\n- Presets creation\n\n4. Common Mistakes to Avoid\n- Over-processing\n- Unnatural skin tones\n- Heavy-handed effects',
            'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTD8_Gv6_B6n7mlcDuBEZNUf96ELq2PsALihx8TwL7IPkesmBhpH95JZWL9NrsbHZXvlhg&usqp=CAU',
            'author': 'Mike Wilson',
            'date': '2024-03-13'
        }
    }
    
    blog = blogs.get(blog_id)
    if blog is None:
        return redirect('blog')
        
    return render(request, 'blog_detail.html', {'blog': blog})

def process_booking(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date_time = request.POST.get('date_time')
        payment_method = request.POST.get('payment_method')

        return HttpResponse(f"Thank you {first_name} {last_name}, your booking for {service} on {date_time} has been received! Payment method: {payment_method}.")
    else:
        return redirect('booking')
