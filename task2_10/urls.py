from django.urls import path
from task2_10 import views


urlpatterns = [
    path("list/", views.VacancyFilterView.as_view()),
]
