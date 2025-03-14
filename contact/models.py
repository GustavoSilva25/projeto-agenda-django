from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = [
            '-id',
        ]


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='contact_picture/%Y/%m/', blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        ordering = [
            '-id',
        ]
