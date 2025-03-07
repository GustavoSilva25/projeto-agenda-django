from django.forms import ModelForm
from django.core.exceptions import  ValidationError

from contact.models import Contact



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['show', 'owner']

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