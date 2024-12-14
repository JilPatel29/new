# Add these imports at the top
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Add this new view
def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})