from django.urls import path
from . import views

urlpatterns = [
    path("encode/", views.encode_url, name="encode_url"),
    path("decode/", views.decode_url, name="decode_url"),
    path("<url_id>/", views.redirect_short_url, name="redirect_short_url"),
]
