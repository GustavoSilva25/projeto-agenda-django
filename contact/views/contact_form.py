from django.shortcuts import render, get_object_or_404, redirect
from  contact.form import ContactForm
from contact.models import Contact

def create(request):

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'title': 'Create contact',
        'hide_header_footer': True,
    }

    return render(
        request,
        'contact/create.html',
        context

    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:single-contact',contact_id=contact_id )
    else:
        form = ContactForm(instance=contact)

    context = {
        'title': 'Update',
        'form': form,
        'hide_header_footer': True,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    confirm_delete = request.POST.get('confirm')

    if request.method == "POST":
        if confirm_delete == 'yes':
            contact.delete()
            return redirect('contact:index')
        
        elif confirm_delete == 'no':
            return redirect('contact:single-contact', contact_id=contact_id)
        
    context = {
        'confirm': confirm_delete,
        'contact': contact,
        'hide_header_footer': True,
    }

    return render(
        request,
        'contact/confirm-delete.html',
        context
    )
