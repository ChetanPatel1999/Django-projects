from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student

@receiver(post_save, sender=Student)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Welcome to Hello World Institute!',
            message=f'Hi {instance.name},\n\nWelcome to Hello World Institute! We are excited to have you join our community.\n\nBest regards,\nThe Hello World Institute Team',
            from_email='chetan8085patel@gmail.com',
            recipient_list=[instance.email],
        )
        print(f"Welcome email sent to {instance.email} for student {instance.name}.")