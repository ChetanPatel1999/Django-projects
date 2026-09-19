from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # 11
    paginator = Paginator(posts, 2)  # Display 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})