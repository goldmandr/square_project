from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import PropertiesListViewList, PropertiesListViewGrid, EstateView

urlpatterns = [
    path('properties_list/<int:page>/', PropertiesListViewList.as_view(), name='properties-list-page'),
    path('properties_grid/<int:page>/', PropertiesListViewGrid.as_view(), name='properties-grid-page'),
    path('properties_list/', RedirectView.as_view(url=reverse_lazy('properties-list-page', kwargs={'page': 1})), name='properties-list'),
    path('properties_grid/', RedirectView.as_view(url=reverse_lazy('properties-grid-page', kwargs={'page': 1})), name='properties-grid'),
    path('estate/<int:pk>/', EstateView.as_view(), name='estate'),
    path('', RedirectView.as_view(url=reverse_lazy('properties-list-page', kwargs={'page': 1})), name='app')
]
