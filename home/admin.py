from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Service
from .models import Payment
from .models import Blog
from .models import Gallery
from .models import ContactUs
from .models import Package
from .models import Booking
from .models import Testimonial
from .models import CustomUser

# Register CustomUser with the UserAdmin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'phone_number', 'profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )

# Register your models here
admin.site.register(Service)
admin.site.register(Payment)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Testimonial)

# Add custom admin for ContactUs
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)