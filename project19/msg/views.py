from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    messages.info(request, "This is a info message.")
    messages.success(request, "This is a success message.")
    messages.warning(request, "This is a warning message.")
    messages.error(request, "This is a error message.")
    messages.debug(request, "This is a debug message.")
    return render(request, 'msg.html')
