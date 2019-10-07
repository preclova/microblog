from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from .views import RegistrationView


app_name = 'accounts'

urlpatterns = [
    # reverse()
    # {% url 'accounts:register' %} -> '/accounts/register'
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegistrationView.as_view(), name='register'),
]
