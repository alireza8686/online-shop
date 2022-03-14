from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Contact
# Create your views here.


def contact(request):
    # settings = Information.objects.first()
    # working_hours = WorkingHours.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data.get("full_name")
            email = contact_form.cleaned_data.get("email")
            subject = contact_form.cleaned_data.get("subject")
            text = contact_form.cleaned_data.get("text")

            contact = Contact.objects.create(full_name=full_name, email=email, subject=subject, text=text)
            contact.save()
            return redirect('contact')
    else:
        contact_form = ContactForm()
        context = {
            "form": contact_form,
            # "setting": settings,
            # "working_hours": working_hours
        }
        return render(request, "contact/contact.html", context)