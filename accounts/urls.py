# coding=utf-8

from .views import *
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', EmailLoginView.as_view(), name="email-login"),
    path('profile/', ProfileView.as_view(), name="profile-url"),
    path('forgot-password/', ForgotPasswordView.as_view(), name="forgot-password-url"),
    path('change-password/token=(?P<token>\w+)', ChangePasswordView.as_view(), name="change-password-url"),
    path('confirm-registration/token=(?P<token>\w+)', ConfirmRegistrationView.as_view(), name="confirm-registration-url"),
    path('registration/', RegistrationView.as_view(), name="registration-url"),
    path('logout/', LogoutView.as_view(), name="logout-view"),
    path('switch_user/', SwitchUser.as_view(), name="switch-user-url"),
    path('google/callback/', GoogleAuthView.as_view(), name="google-callback-url"),
]
