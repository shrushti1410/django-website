from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings
def index(request):
    message = None  # Default message

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        user_message = request.POST.get("message")

        # Save to database
        Contact.objects.create(name=name, email=email, message=user_message)

        # Send email notification
        send_mail(
            subject="New Contact Form Submission",
            message=f"Name: {name}\nEmail: {email}\nMessage: {user_message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # Send to yourself
            fail_silently=False,
        )

        # Send confirmation email to user
        send_mail(
            subject="Thank You for Contacting Us!",
            message=f"Dear {name},\n\nThank you for reaching out. We will get back to you soon.\n\nBest Regards,\nEmpire Export",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # Send to user
            fail_silently=False,
        )

        # Success message
        message = "Thank you for reaching us!"

    return render(request, "index.html", {"message": message})