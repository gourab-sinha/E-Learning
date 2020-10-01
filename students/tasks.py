from celery import task
from django.core.mail import send_mail
from ELearning.settings import EMAIL_HOST_USER


@task
def course_registered(student):
    print(os.environ.get('DJANGO_EMAIL'))
    subject = f'Course Registration'
    message = f'Dear {student["first_name"]}, \n\n' \
              f'You have successfully registered for the course {student["course"]}.'
    mail_sent = send_mail(subject, message, EMAIL_HOST_USER, [student['email']])

    return mail_sent
