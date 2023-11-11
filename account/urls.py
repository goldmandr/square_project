from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import ProfileView, ChangePasswordProcessView

urlpatterns = [
    path('profile/change_password/', ChangePasswordProcessView.as_view(), name='profile-change-view'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', RedirectView.as_view(url=reverse_lazy('profile')), name='account')
]
