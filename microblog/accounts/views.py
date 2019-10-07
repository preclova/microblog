from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().dispatch(request, *args, **kwargs)
