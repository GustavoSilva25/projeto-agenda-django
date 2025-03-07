from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

