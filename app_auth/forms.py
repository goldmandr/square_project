from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.forms.widgets import EmailInput
from django.core.validators import EmailValidator


class AppLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AppLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Ваш e-mail'
        self.fields['username'].widget = EmailInput(attrs={'placeholder': 'E-mail'})
        self.fields['username'].validators.append(EmailValidator)

        self.fields['password'].label = 'Ваш пароль'
        self.fields['password'].widget.attrs['placeholder'] = 'Пароль'


class AppUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AppUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Ваш e-mail'
        self.fields['username'].widget = EmailInput(attrs={'placeholder': 'E-mail'})
        self.fields['username'].validators.append(EmailValidator)

        self.fields['password1'].label = 'Ваш пароль'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'

        self.fields['password2'].label = 'Повтор пароля'
        self.fields['password2'].widget.attrs['placeholder'] = 'Пароль'


class AppPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(AppPasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = 'Ваш e-mail'
        self.fields['email'].widget = EmailInput(attrs={'placeholder': 'E-mail'})

