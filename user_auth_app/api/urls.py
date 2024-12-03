from django.urls import path
from user_auth_app.api.views import RegistrationView, CustomLoginView

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration-view'),
    path('login/', CustomLoginView.as_view(), name='login')
]