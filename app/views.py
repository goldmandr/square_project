from urllib.parse import urlparse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import resolve

from area_parser.models import Realestate

# temporary, until the database structure is updated
resources_domains = {
    'kf.expert': 'kf',
    '%D0%B4%D0%BE%D0%BC.%D1%80%D1%84': 'dom_rf'
}


class PropertiesListView(ListView):
    context_object_name = 'realestates'
    paginate_by = 12
    ordering_types = [
        {'value': '0', 'label': 'По умолчанию', 'sort_by': 'pk'},
        {'value': '1', 'label': 'По названию (возрастание)', 'sort_by': 'title'},
        {'value': '2', 'label': 'По названию (убывание)', 'sort_by': '-title'},
        {'value': '3', 'label': 'По площади (возрастание)', 'sort_by': 'price__area'},
        {'value': '4', 'label': 'По площади (убывание)', 'sort_by': '-price__area'},
        {'value': '5', 'label': 'По стоимости (возрастание)', 'sort_by': 'price__price'},
        {'value': '6', 'label': 'По стоимости (убывание)', 'sort_by': '-price__price'},
        {'value': '7', 'label': 'По стоимости за м² (возрастание)', 'sort_by': 'pricepersquaremeter'},
        {'value': '8', 'label': 'По стоимости за м² (убывание)', 'sort_by': '-pricepersquaremeter'}
    ]

    def get_queryset(self):
        query_set = Realestate.objects.all()
        if (self.request.GET.get('cost_from') is not None) and (self.request.GET.get('cost_from').isdigit()):
            query_set = query_set.filter(price__price__gte=self.request.GET.get('cost_from'))
        if (self.request.GET.get('cost_to') is not None) and (self.request.GET.get('cost_to').isdigit()):
            query_set = query_set.filter(price__price__lte=self.request.GET.get('cost_to'))
        if (self.request.GET.get('square_from') is not None) and (self.request.GET.get('square_from').isdigit()):
            query_set = query_set.filter(price__area__gte=self.request.GET.get('square_from'))
        if (self.request.GET.get('square_to') is not None) and (self.request.GET.get('square_to').isdigit()):
            query_set = query_set.filter(price__area__lte=self.request.GET.get('square_to'))
        if (self.request.GET.get('ordering') is not None) and (int(self.request.GET.get('ordering')) < len(self.ordering_types)):
            query_set = query_set.order_by(self.ordering_types[int(self.request.GET.get('ordering'))]['sort_by'])
        return query_set

    def get_context_data(self, **kwargs):
        context = super(PropertiesListView, self).get_context_data(**kwargs)

        paginator = context['paginator']
        page_obj = context['page_obj']
        pages_list = [1]
        if paginator.num_pages < 6:
            pages_list += [i + 2 for i in range(4) if i <= paginator.num_pages - 2]
            pages_list += [0 for i in range(5 - paginator.num_pages)]
        elif page_obj.number < 4:
            pages_list += [2, 3, 4, paginator.num_pages]
        elif page_obj.number >= paginator.num_pages - 2:
            pages_list += [paginator.num_pages - 3, paginator.num_pages - 2, paginator.num_pages - 1, paginator.num_pages]
        else:
            pages_list += [page_obj.number - 1, page_obj.number, page_obj.number + 1, paginator.num_pages]

        context['pages_list'] = pages_list
        context['ordering_options'] = self.ordering_types
        return context


class PropertiesListViewList(LoginRequiredMixin, PropertiesListView):
    template_name = 'app/properties_list.html'
    extra_context = {'page_title': 'Главная', 'list_type': 'list'}


class PropertiesListViewGrid(LoginRequiredMixin, PropertiesListView):
    template_name = 'app/properties_grid.html'
    extra_context = {'page_title': 'Главная', 'list_type': 'grid'}


class EstateView(LoginRequiredMixin, DetailView):
    template_name = 'app/estate.html'
    extra_context = {'page_title': 'Недвижимость'}

    model = Realestate
    context_object_name = 're'
    
    def get_context_data(self, **kwargs):
        context = super(EstateView, self).get_context_data(**kwargs)
        direct_link = self.get_object().directlink.link
        if direct_link:
            context['resource_provider'] = resources_domains[urlparse(direct_link).netloc]
        else:
            context['resource_provider'] = None

        context['back_link'] = self.request.META.get('HTTP_REFERER')
        return context
