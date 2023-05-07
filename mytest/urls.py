from django.urls import path
from . import views

urlpatterns = [
    path('',  views.polling_unit_result, name='polling_unit_result'),
]
 