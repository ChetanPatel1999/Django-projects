from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from .models import Channel
# Create your views here.
# def channel_list(request):
#     channel = cache.get('channel')
#     if not channel:
#         channel = Channel.objects.first()
#         cache.set('channel', channel, timeout=300)  # Cache for 5 minutes
#         print("Data fetched from database ")
#     else:
#         print("Data fetched from cache ")    
#     return render(request, 'youtube/channel_list.html', {'channel': channel})

# def cache_delete(request):
#     cache.delete('channel')
#     return HttpResponse("Cache deleted successfully.")



#per view caching
# from django.views.decorators.cache import cache_page
# @cache_page(60)  # Cache for 15 minutes
# def channel_list(request):
#     print("Data fetched from database ")
#     channel = Channel.objects.first()
#     return render(request, 'youtube/channel_list.html', {'channel': channel})


#template fragment caching
def channel_list(request):
    channel = Channel.objects.first()
    return render(request, 'youtube/channel_list.html', {'channel': channel})