from rest_framework import serializers
from charts.models import ExampleModel


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = ('firstName', 'lastName')
