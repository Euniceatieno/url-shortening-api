from django.urls import path
from . import views

urlpatterns = [
    path("encode/", views.encode_url),
    path("decode/", views.decode_url),
]
