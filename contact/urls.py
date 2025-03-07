from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from contact import views


app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    #CRUD
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/detail/', views.single_contact, name='single-contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)