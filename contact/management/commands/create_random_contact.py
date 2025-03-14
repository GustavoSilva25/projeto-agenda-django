from pathlib import Path
import os
import sys
import django
from random import choice



DJANGO_BASE_DIR =  Path(__file__).parent.parent

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
sys.path.append(str(DJANGO_BASE_DIR))
django.setup()

from faker import Faker
from contact.models import Contact, Category
from django.db import transaction

class CreateRandomContact():
    
    def __init__(self, number_of_object):
        self.faker = Faker()
        self.number_of_object = number_of_object

    def generate_random_contact(self):
        first_name, last_name = self.faker.name().split(' ', 1)
        email = self.faker.email()
        phone = self.faker.phone_number()
        description = self.faker.text(max_nb_chars=185)
        
        categories_list = ['Family', 'Friends', 'Suppliers', 'Others']
        category_name  = choice(categories_list)

        category, _ = Category.objects.get_or_create(name=category_name)


        return Contact(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    description=description,
                    category=category
                )



    def save(self):
        try:
            contacts = []
            for _ in range(self.number_of_object):
                contact = self.generate_random_contact()
                contacts.append(contact)
                
            with transaction.atomic():
                Contact.objects.bulk_create(contacts)

        except Exception as error:
            print(f'error creating contact! {error}')




if __name__ == '__main__':
    create_contact = CreateRandomContact(number_of_object=50)
    create_contact.save()
