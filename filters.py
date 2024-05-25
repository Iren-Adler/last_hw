import django_filters
from core import models

class Programmer(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Имя', lookup_expr='icontains')
    birthday_to = django_filters.DateFilter(field_name='birthday', loolup_expr='lt', label='День рождения по')
    salary_from = django_filters.NumberFilter(field_name='salary', lookup_expr='gt', label='Зарплата от')

    fio = django_filters.CharFilter(method='fio_filter')
    class Meta:
        model = models.Programmer
        exclude = ('photo',)

    def fio_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(surname__icontains=value) | Q(potronymic__icontains=value))
