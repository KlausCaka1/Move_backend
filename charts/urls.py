from django.urls import path
from charts.views import ExampleModelView

urlpatterns = [
    path('get-charts/', ExampleModelView.as_view(), name='example-model')
]
