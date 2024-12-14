from django.contrib import admin
from django.urls import include, path
from home import views  # Import views from the home app

urlpatterns = [
    path('', views.index, name='index'),  # The root URL will load index.html
    path('home/', views.home, name='home'),  # /home/ will also load index.html
    path('gallery/', views.gallery, name='gallery'),  # /gallery/ will load gallery.html
    path('contact/', views.contact, name='contact'),  # /contact/ will load contact.html
    path('services/', views.services, name='services'),  # /services/ will load home.html
    path('booking/', views.booking, name='booking'),  # /services/ will load home.html
    path('process-booking/', views.process_booking, name='process_booking'),
    # path('blog/', views.blog, name='blog'),
     path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
     path('signup/', views.signup_view, name='signup'),
     path('login/', views.login_view, name='login'), 
    path('', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),  # Include the admin URL
    # path('', include('home.urls')),     

]
