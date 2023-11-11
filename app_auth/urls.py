from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, LogoutView

from .views import AppLoginView, AppRegisterView, AppRegisterConfirmView, AppPasswordResetView,\
    AppPasswordResetConfirmView


urlpatterns = [
    path('login/', AppLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('register/', AppRegisterView.as_view(), name='register'),
    path('register_confirm/<int:pk>/<str:email_code>/', AppRegisterConfirmView.as_view(), name='register_confirm'),
    path('password_reset/', AppPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html', extra_context={'page_title': 'Отправка подтверждения'}), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', AppPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html', extra_context={'page_title': 'Пароль установлен'}), name='password_reset_complete'),
    path('', RedirectView.as_view(url=reverse_lazy('login')))
]