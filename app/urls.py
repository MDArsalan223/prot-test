from django.urls import path
from .views import contact_view, index
from app import views

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
]
