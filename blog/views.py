from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    blog_count = Blog.objects.count()
    blogs = Blog.objects.order_by ('-pub_date').all()[:10]
    return render(request, 'blogs/all_blogs.html', {'blogs':blogs,'blog_count':blog_count})

def detail(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
