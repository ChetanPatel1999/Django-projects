from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage,send_mass_mail
from django.template.loader import render_to_string

# Create your views here.
# def sending_email(request):
#     print("hello python")
#     subject='Welcome to Hello World Institute'
#     message="""
#      Hello Student,
#      Welcome to Hello World Institute. 
#      Thank you for joining our course.
#      Regards,
#      Hello World Institute
#      """
#     from_email="chetan8085patel@gmail.com"
#     reciver_email=["rydhampatel83@gmail.com","mohitrathore143m@gmail.com","hweduinstitute@gmail.com"]
#     send_mail(subject,message,from_email,reciver_email,fail_silently=False )
#     return HttpResponse("<h1>gmail send succefully !</h1>")


# def sending_email(request):
#     html_content = render_to_string('email/welcome.html', {'name': 'Rajveer'})
#     email = EmailMessage(
#         subject='Welcome to Hello World Institute',
#         body=html_content,
#         from_email='chetan8085patel@gmail.com',
#         to=['rydhampatel83@gmail.com', 'mohitrathore143m@gmail.com', 'hweduinstitute@gmail.com']
#     )
#     email.content_subtype = "html"
#     email.send()
#     return HttpResponse("<h1>template gmail send successfully !</h1>")



# mass mail sending
def sending_email(request):
    message= (
        (
             'Python Batch Starting', 
             'Our new Python batch is starting from Monday.', 
             'chetan8085patel@gmail.com',
             ['rydhampatel83@gmail.com', 'mohitrathore143m@gmail.com']
        ),
        (
           'Holiday Notice', 
           'The institute will remain closed tomorrow.', 
            'chetan8085patel@gmail.com',
            ['hweduinstitute@gmail.com', 'ys066893@gmail.com']
        )
           )
    send_mass_mail(message)
    return HttpResponse("<h1>mass gmail send successfully !</h1>")
    
