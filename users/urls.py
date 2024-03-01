from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, VerifyEmail, \
    EmailConfirmationSentView, EmailConfirmedView, EmailConfirmationFailedView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('confirm-email/<str:uidb64>/<str:token>/', VerifyEmail.as_view(), name='verify_email'),
    path('email-confirmation-sent', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('email-confirm-failed', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
]
