from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def sending_email(request):
    print("hello python")
    subject='Welcome to Hello World Institute'
    message="""
     Hello Student,
     Welcome to Hello World Institute. 
     Thank you for joining our course.
     Regards,
     Hello World Institute
     """
    from_email="chetan8085patel@gmail.com"
    reciver_email=["rydhampatel83@gmail.com","mohitrathore143m@gmail.com","hweduinstitute@gmail.com"]
    send_mail(subject,message,from_email,reciver_email,fail_silently=False )
    return HttpResponse("<h1>gmail send succefully !</h1>")
