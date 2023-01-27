from django.urls import path
from . import views

urlpatterns = [
    path('process_command/', views.process_command, name='process_command'),
]
