from django.urls import path
from .views import index, next_view


urlpatterns = [
    path('', index),
    path('next', next_view)
]