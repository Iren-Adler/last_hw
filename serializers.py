from rest_framework import serializers

from core import models

class Programmer(serializers.ModelSerializer):
    fio = serializers.SerializerMethodField()
    class Meta:
        model = models.Programmer
        fields = "__al__"
    def get_fio(self, obj: models.Programmer):
        return obj.get_full_name()
    def validate(self, attrs, dict):
        if attrs['salary'] < 0:
            raise ValidationError('Зарплата должна быть неотрицательной')
        return attrs