from django.conf import settings
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView

from wykop.accounts.forms import RegisterForm


class LogoutRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL))
        return super().dispatch(request, *args, **kwargs)


class RegisterView(LogoutRequiredMixin, FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('posts:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LogoutRequiredMixin, LoginView):
    template_name = 'login.html'
