from django.core.mail import send_mail
from django.conf import settings


def create_user_emailing(email, password):
    send_mail(
        "Your password from 'adminka' system",
        f"Use this password to login to the system.\nYou'll be able to change your password at any time in account settings \n {password}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
