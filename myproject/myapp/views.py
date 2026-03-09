from django.shortcuts import render

# Home page
def home(request):
    return render(request, 'myapp/home.html')

# Products page
def products(request):
    return render(request, 'myapp/products.html')

# Our Story page
def our_story(request):
    return render(request, 'myapp/our_story.html')

def services(request):
    return render(request, 'myapp/services.html')

# Contact page
def contact(request):
    return render(request, 'myapp/contact.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Message from {name}"

        body = f"""
You have received a new contact message.

Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject,
            body,
            email,  # 👈 FROM: USER EMAIL
            ['uzhavarchoice@gmail.com'],  # 👈 TO: ADMIN
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'myapp/contact.html')
