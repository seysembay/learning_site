from django.conf import settings
from django.core.mail import send_mail


def send_to_admin(name, email, message):
    subject = 'Новое сообщение от {}'.format(name)
    message_body = 'Сообщение от {}: {}'.format(email, message)
    send_mail(subject, message_body, settings.EMAIL_HOST_USER, ['beket100796@bk.ru'])


def send_to_user(email, message):
    subject = 'Новое сообщение от EDUCATIONIT'
    message_body = 'Ваше сообщение получено: {}'.format(message)
    send_mail(subject, message_body, settings.EMAIL_HOST_USER, [email])
