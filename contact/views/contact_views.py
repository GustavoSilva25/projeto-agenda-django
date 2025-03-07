from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact
# Create your views here.


def index(request):
    contact_list = Contact.objects.filter(
        show=True,
    )
    paginator = Paginator(contact_list, 10) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'title': 'agenda',
        'page_obj' : page_obj,
    }


    return render(
        request,
        'contact/index.html',
        context,
    )


def search(request):
    q = request.GET.get('q').strip()

    if q == "":
        return redirect("contact:index")

    contact = Contact.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) |
        Q(email__icontains=q) |
        Q(phone__icontains=q)
    )

    paginator = Paginator(contact, 10) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'title': 'search',
        'page_obj' : page_obj,
    }


    return render(
        request,
        'contact/index.html',
        context,
    )


def single_contact(request, contact_id):
    contact = get_object_or_404(Contact, show=True, pk=contact_id)

    context = {
        'title': f'{contact.first_name} {contact.last_name}',
        'contact' : contact,
    }


    return render(
        request,
        'contact/single-contact.html',
        context,
    )

        
