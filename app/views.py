from django.shortcuts import render
from app.models import Contact

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def contact_view(request):
    success_message = None  # Initialize success message variable

    if request.method == 'POST':
        email = request.POST.get('email')
        contact = Contact.objects.create(email=email)
        success_message = 'Thank you for your submission!'  # Set the success message

    return render(request, 'app/index.html', {'success_message': success_message})