from django.shortcuts import render
from .models import Post
from django.db.models import Q
# Create your views here.
def post_list(request):
    categories = Post.objects.values_list('category', flat=True).distinct()
    posts=Post.objects.all()
    search = request.GET.get('search','')
    search_category = request.GET.get('category','')
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
    if search_category:
        posts = posts.filter(category=search_category)
    return render(request, 'blog/post_list.html',{'posts':posts,'search':search,'search_category':search_category,'categories':categories})
