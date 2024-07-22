from django.urls import path
from .views import sign_up_by_django

urlpatterns = [
    path('signup/', sign_up_by_django, name='signup_by_django'),
]