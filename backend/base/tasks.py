# base/tasks.py

from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings


@shared_task()
def send_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        settings.EMAIL_HOST,
        [email_address],
        fail_silently=False,
    )
