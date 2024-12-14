# Add this new URL pattern
path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),