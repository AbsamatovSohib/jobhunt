from task2_10.models import Vacancy


class MyFilter(django_filters.FilterSet):
    salary_from = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_to = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='exact')

    class Meta:
        model = Vacancy
        fields = ("salary", "salary_from", "salary_to")
