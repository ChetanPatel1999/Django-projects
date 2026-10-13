from django.shortcuts import render
from django.core.cache import cache
from .models import Channel

# Create your views here.
def channel_list(request):
    channel = cache.get('channel')
    if not channel:
        channel = Channel.objects.first()
        cache.set('channel', channel, timeout=300)  # Cache for 5 minutes
        print("Data fetched from database ")
    else:
        print("Data fetched from cache ")    
    return render(request, 'youtube/channel_list.html', {'channel': channel})