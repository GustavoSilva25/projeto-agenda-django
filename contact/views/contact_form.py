from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from contact.form import ContactForm
from django.http import Http404

from contact.models import Contact


@login_required(login_url='contact:login')
def create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
    else:
        form = ContactForm()

    context = {
        'form': form,
        'title': 'Create contact',
        'hide_header_footer': True,
    }

    return render(request, 'contact/create.html', context)


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.user != contact.owner:
        raise Http404('You do not have to permission to edit this contact')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact:single-contact', contact_id=contact_id)
    else:
        form = ContactForm(instance=contact)

    context = {
        'title': 'Update',
        'form': form,
        'hide_header_footer': True,
    }

    return render(request, 'contact/create.html', context)



@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.user != contact.owner:
        raise Http404('You do not have to permission to delete this contact')

    confirm_delete = request.POST.get('confirm')

    if request.method == 'POST':
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

    return render(request, 'contact/confirm-delete.html', context)
