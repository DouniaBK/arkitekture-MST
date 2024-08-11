import logging
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
import environ

env = environ.Env()
environ.Env.read_env()

logger = logging.getLogger(__name__)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                # Send email
                body = """Hello,

                        This is a multiline email sent from Django.

                        Here are the details:
                        - Point 1: Information about point 1.
                        - Point 2: Information about point 2.
                        - Point 3: Information about point 3.

                        Best regards,
                        Your Company Name
                        """

                email = EmailMessage('Hello', body, "douniazedbacha@gmail.com", ["douniazedbacha@gmail.com",])

                if email.send():
                    print(" ------------------ YEEEAAAAHHHHHHH ------------------")
                else: 
                    print(" ------------------ NAAAAAAAAAAAAAA ------------------")

                '''
                send_mail(
                    f"Contact Form Submission from {name}",
                    message,
                    "douniazedbacha@gmail.com",
                    ['douniazedbacha@gmail.com',]
                )'''
                
                #return redirect("contact_success")
            except Exception as e:
                logger.error(
                    "Error sending contact form email to Architekturbüro Starke-Thomsen",
                    exc_info=True,
                )
                # Optional: You can add a message to notify the
                # user that an error occurred
                form.add_error(
                    None,
                    "An error occurred while sending your message. Please send an email direclty to info@architektur-starke-thomsen.de.",
                )
    else:
        form = ContactForm()
    return render(request, "home/contact.html", {"form": form})


def contact_success_view(request):
    return render(request, 'home/contact_success.html')


def home_view(request):
    return render(request, "home/home.html")


def about_view(request):
    return render(request, "home/about.html")


def services_view(request):
    return render(request, "home/services.html")


def portfolio_view(request):
    return render(request, "home/portfolio.html")


def footer_view(request):
    return render(request, "home/footer.html")


def terms_view(request):
    return render(request, "home/terms.html")


def privacy_view(request):
    return render(request, "home/privacy.html")


def disclaimer_view(request):
    return render(request, "home/disclaimer.html")


def impressum_view(request):
    return render(request, "home/impressum.html")


def projectone_view(request):
    return render(request, "home/projectone.html")


def projecttwo_view(request):
    return render(request, "home/projecttwo.html")


def send_test_email(request):
    subject = 'Test Email'
    message = 'This is a test email sent from Django.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER, ]  # Replace with your email or test recipient
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Test email sent.")
