from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
def home(request):
    time = datetime.now()
    posts  = Post.objects.order_by('-pub_date')
    context = {
        'posts': posts,
        'time': time
    }
    return render(request, 'posts/home.html', context)
@login_required
def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/posts_detail.html', {'post':post})
