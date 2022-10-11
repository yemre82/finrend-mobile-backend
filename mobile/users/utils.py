from django.core.mail import EmailMultiAlternatives
from mobile import settings
import random
import math

def send_email(to_email, otp, subject):
    otp = str(otp)
    subject, from_email, to_email = subject, settings.EMAIL_HOST_USER, to_email
    text_content = 'Enter for the verification :' + otp
    html_content = '<p>Enter for the verification :</p> <h3>' + otp + '</h3>'
    msg = EmailMultiAlternatives(subject, text_content,'FINREND <'+ from_email+'>', [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_email_forgot_password(to_email, otp, subject):
    otp = str(otp)
    subject, from_email, to_email = subject, settings.EMAIL_HOST_USER, to_email
    text_content = 'Enter for the verification :' + otp
    html_content = '<p>Enter for the verification :</p> <h3>' + otp + '</h3>'
    msg = EmailMultiAlternatives(subject, text_content,'FINREND <'+ from_email+'>', [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def generate_random_num():
    random_str = ""
    digits = [i for i in range(0, 10)]
    for i in range(4):
        index = math.floor(random.random()*10)
        random_str += str(digits[index])
    return random_str