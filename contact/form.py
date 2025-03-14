from django.forms import ModelForm
from django.core.exceptions import  ValidationError
from django.contrib.auth.forms import UserCreationForm


from contact.models import Contact
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import password_validation


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=2,
    )
    last_name = forms.CharField(
        required=True,
        min_length=2,
    )

    email = forms.EmailField(
        required=True,
    )

    
    def clean_email(self):
        email = self.cleaned_data.get('email')


        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError(
                    'existing email!'
                )
            )
        return email

    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'email', 'password1', 'password2',
        )

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=2,
        help_text="Required. Minimum 2 characters.",
    )
    last_name = forms.CharField(
        required=True,
        min_length=2,
        help_text="Required. Minimum 2 characters.",
    )
    email = forms.EmailField(
        required=True,
        help_text="Required. Enter a valid email address.",
    )

    password1 = forms.CharField(
        label="Password",
        required=False,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": 'new_password'}),
        help_text= password_validation.password_validators_help_text_html,
    )

    password2 = forms.CharField(
        label="Password 2",
        required=False,
        widget=forms.PasswordInput(attrs={"autocomplete": 'new_password'}),
    )


    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)


        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()
            


    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        "passwords don't match"
                    )
                )

        return super().clean()

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as error:
                self.add_error(
                    'password1',
                    error,
                )

        return password1


    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email', ValidationError(
                        'existing email!'
                    )
                )
        return email
    

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username',
            'email', 'password1', 'password2'
        )



class ContactForm(ModelForm):
    
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update(
            {
                'accept': 'image/*',
            }
        )



    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name and len(first_name) < 2:
            raise ValidationError("O nome tem que ser maior que 2 caracteres")
        return first_name
    

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name and len(last_name) < 2:
            raise ValidationError("O sobrenome tem que ser maior que 2 caracteres")
        return last_name
    
    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name:
            if first_name == last_name:
                self.add_error('last_name', 'O nome e sobrenome não podem ser iguais')

        return cleaned_data

    class Meta:
        model = Contact
        exclude = ['show', 'owner']