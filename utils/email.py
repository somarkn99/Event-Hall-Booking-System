from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_notification_email(to_email, subject, template_name, context):
    html_message = render_to_string(template_name, context)
    plain_message = context.get('plain_message', '')

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        fail_silently=False,
        html_message=html_message
    )
