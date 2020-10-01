from celery import task
from django.core.mail import send_mail
from ELearning.settings import EMAIL_HOST_USER


@task
def content_added(information):

    subject = f'Course Registration'
    message = f'Dear {information["name"]}, \n\n' \
              f'You have successfully added content {information["content"]} to module {information["module"]}' \
              f' of course {information["course"]}. Thank you.'
    mail_sent = send_mail(subject, message, EMAIL_HOST_USER, [information['email']])

    return mail_sent






