from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.views import PasswordContextMixin
from django.contrib.auth import update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'
    extra_context = {'page_title': 'Профиль'}

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['email'] = User.objects.get(pk=self.request.user.id).email
        context['change_password_form'] = PasswordChangeForm(self.request.user)
        context['back_link'] = self.request.META.get('HTTP_REFERER')
        return context


class ChangePasswordProcessView(ContextMixin, PasswordContextMixin, TemplateResponseMixin, ProcessFormView):
    template_name = 'account/profile.html'
    extra_context = {'page_title': 'Профиль'}

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(self.request.user, self.request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one.
            update_session_auth_hash(self.request, form.user)

            messages.add_message(request, messages.SUCCESS, 'Пароль успешно обновлен!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        else:
            messages.add_message(request, messages.ERROR, 'Неверный старый или некорректный новый пароль')
            return HttpResponseRedirect(reverse_lazy('profile'))

    def get_context_data(self, **kwargs):
        context = super(ChangePasswordProcessView, self).get_context_data(**kwargs)
        context['email'] = User.objects.get(pk=self.request.user.id).email
        return context
