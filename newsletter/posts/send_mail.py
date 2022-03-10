from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def create_and_send_mail(subject: str, context: dict, recipient_list: list):
    # {'context': 'values'}
    html_message = render_to_string('test_template.html', context)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER

    mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)