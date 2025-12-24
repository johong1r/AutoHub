from django.urls import path
from .api import (custom_login,
                custom_register,
                custom_logout,
                test_email_send,
                # reset_password_confirm,
                # reset_password_request,
                # reset_password_verify,
                profile,
                change_password,
)
from .generic_api import (ResetPasswordRequestView,
                          ResetPasswordVerifyView,
                          ResetPasswordConfirmView
)

urlpatterns = [
    path('login/', custom_login, name='custom-login'),
    path('register/', custom_register, name='custom-register'),
    path('logout/', custom_logout, name='custom-logout'),
    path('test-email-send/', test_email_send, name='test-email-send'),
    path('reset-password/request/', ResetPasswordRequestView.as_view(), name='reset-password-request'),
    path('reset-password/verify/', ResetPasswordVerifyView.as_view(), name='reset-password-verify'),
    path('reset-password/confirm/', ResetPasswordConfirmView.as_view(), name='reset-password-confirm'),
    path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change-password'),
]   