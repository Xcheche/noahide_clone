from urllib import request
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    time = datetime.now()
    posts = Post.objects.order_by('-pub_date')  # Get all posts
    paginator = Paginator(posts, 3)  # Paginate with 3 posts per page
    page_number = request.GET.get('page')  # Get current page number from URL
    page_obj = paginator.get_page(page_number)  # Get Page object for the current page

    # Search logic
    search_query = request.GET.get('search', '')  # Get the search query from the 'search' parameter
    if search_query != '' and search_query is not None:
        posts = posts.filter(title__icontains=search_query)  # Filter posts by title containing the search query
        paginator = Paginator(posts, 3)  # Re-paginate filtered posts
        page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,  # Pass paginated posts
        'page_obj': page_obj,  # Essential for template pagination logic
        'is_paginated': page_obj.has_other_pages(),  # Check if pagination is needed
        'time': time,
    }
    return render(request, 'posts/home.html', context)

@login_required
def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/posts_detail.html', {'post': post})
