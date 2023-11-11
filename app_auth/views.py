from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
import random
import string

from django.contrib.auth.models import User
from .models import UserAccount
from .forms import AppLoginForm, AppUserCreationForm, AppPasswordResetForm


def gen_random_string(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])


class AppLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = AppLoginForm
    extra_context = {'page_title': 'Авторизация'}


class AppRegisterView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'page_title': 'Регистрация'}

    def form_valid(self, form):
        result = super(AppRegisterView, self).form_valid(form)
        self.object.email = self.object.username

        self.object.is_active = False
        self.object.save()
        email_code = gen_random_string(64)
        UserAccount.objects.update_or_create(user=self.object, defaults={'user': self.object, 'email_code': email_code})

        # e-mail send
        confirm_link = reverse_lazy("register_confirm", kwargs={'pk': self.object.pk, 'email_code': email_code})
        email = EmailMessage(subject='E-mail confirmation', body=f'Confirmation link: {confirm_link}', to=[form.cleaned_data['username']])
        email.send()

        return result


class AppRegisterConfirmView(TemplateView):
    template_name = 'auth/auth_msg_page.html'
    extra_context = {'page_title': 'Подтверждение регистрации'}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context_message = ''

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])

            if user.useraccount.email_code == self.kwargs['email_code']:
                user.useraccount.email_code = None
                user.useraccount.save()
                user.is_active = True
                user.save()
                self.context_message = 'Спасибо за регистрацию!'
            else:
                self.context_message = 'Ссылка подтверждения устарела или недействительна'
        except ObjectDoesNotExist:
            self.context_message = 'Пользователь не найден'

        return super(AppRegisterConfirmView, self).get(request, *args, **kwargs)


class AppPasswordResetView(PasswordResetView):
    form_class = AppPasswordResetForm
    template_name = 'auth/reset_password.html'
    subject_template_name = 'auth/reset_subject.txt'
    email_template_name = 'auth/reset_email.txt'
    extra_context = {'page_title': 'Сброс пароля'}


class AppPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset_confirm.html'
    extra_context = {'page_title': 'Новый пароль'}

