from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from contact.form import UserForm, UserUpdateForm
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash



def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            auth.login(request, form.instance)
            messages.success(request, "Registration successful")
            return redirect('contact:index')
        else:
            messages.error(request, "Error in registration")
    

    context = {
        'heading': 'Sign up',
        'form': form,

    }
    return render(
        request,
        'contact/user_form.html',
        context,
    )


def user_details(request):
    return render(
        request,
        'contact/profile_details.html',
        context={'hide_header_footer': True,}
    )

def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('contact:index')
        else:
            messages.error(request, "Error!")

    form = AuthenticationForm()

    context = {
        'heading': 'Sign in',
        'form': form,

    }
    return render(
        request,
        'contact/user_form.html',
        context,
    )

def logout(request):
    auth.logout(request)
    return redirect('contact:index')


def update_user(request):

    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = UserUpdateForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Update user success!")
            return redirect('contact:user_details')

        else:
            messages.error(request, "error")


    context = {
        'heading': 'Update user',
        'form': form,
    }
    return render(
        request,
        'contact/user_form.html',
        context,
    )
