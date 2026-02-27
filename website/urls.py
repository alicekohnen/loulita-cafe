from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
    path("menu/<int:item_id>/", views.menu_detail, name="menu_detail"),
]