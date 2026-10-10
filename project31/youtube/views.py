from django.shortcuts import render
from django.core.cache import cache
from .models import Channel
# Create your views here.
def channel_list(request):
    channels = cache.get('channel_list')
    if not channels:
        channels = Channel.objects.all()
        cache.set('channel_list', channels, 300)
        print("Data fetched from database")
    else:
        print("Data fetched from cache")    
    return render(request, 'youtube/channel_list.html', {'channels': channels})