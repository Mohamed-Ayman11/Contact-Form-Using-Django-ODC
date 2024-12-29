from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f"Message from {name} ({email}):\n\n{message}"

            # Send email (printed to console for testing)
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=full_message,
                from_email='test@example.com',  # Dummy email for console
                recipient_list=['recipient@example.com'],  # Dummy recipient
            )
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
