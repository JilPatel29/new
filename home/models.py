from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)  # Use string reference
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    phone = models.CharField(max_length=15, blank=True)
    default='default-profile.png',  # Default image for users without an uploaded image
    address = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Signal handlers
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, default='General')  # Add a default value here
    
    def __str__(self):
        return self.name



class Payment(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)  # e.g., 'Credit Card', 'PayPal'
    status = models.CharField(max_length=20)  # e.g., 'Pending', 'Completed', 'Failed'

    def __str__(self):
        return f"{self.method} - {self.amount} - {self.status}"


class Blog(models.Model):
    # Keep existing fields...
    
    # Add these new fields
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    short_description = models.TextField(max_length=200, blank=True)
    read_time = models.IntegerField(default=5)  # Estimated read time in minutes
    category = models.CharField(max_length=50, default='General')
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])



class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else "Untitled"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # Example: '1 hour', '2 hours', 'Full day'
    features = models.TextField()  # List the features of the package

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    package = models.ForeignKey('Package', on_delete=models.CASCADE)  # Link to Package
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date}"

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5 stars rating
    date_submitted = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=100, default='Anonymous')  # Set a default value here

    def __str__(self):
        return f"{self.customer_name} - {self.rating} stars"
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)  # Link to CustomUser (author)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


