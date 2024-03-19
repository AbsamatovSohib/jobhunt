from rest_framework import serializers
from task2_10 import models


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = ("title", "salary", )
