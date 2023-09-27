from django.urls import path

from . import views

urlpatterns = [
    path("", views.showList, name="list"),
    path("newItem/", views.create_item, name="new_item"),
]