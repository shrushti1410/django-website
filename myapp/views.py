from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Contact
from django.shortcuts import render

def index(request):
    message = None  # Default message

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        user_message = request.POST.get("message")

        # Save to database
        Contact.objects.create(name=name, email=email, message=user_message)

        try:
            # Send email notification to admin
            send_mail(
                subject="New Contact Form Submission",
                message=f"Name: {name}\nEmail: {email}\nMessage: {user_message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,  # Debugging mode
            )

            # Send confirmation email to user
            send_mail(
                subject="Thank You for Contacting Us!",
                message=f"Dear {name},\n\nThank you for reaching out. We will get back to you soon.\n\nBest Regards,\nEmpire Export",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,  # Debugging mode
            )

            message = "Thank you for reaching out!"
            return JsonResponse({"message": message}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "index.html", {"message": message})
