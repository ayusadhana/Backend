from django.urls import path
from .views import user_registration,verify_otp

urlpatterns = [
    path('userRegistration/', user_registration, name='user_registration'),
    path('verify_otp/',verify_otp)
]
