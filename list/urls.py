from django.urls import path

from . import views

urlpatterns = [
    path("", views.showList, name="list"),
    path("newItem/", views.create_item, name="new_item"),
    path("updateItem/<str:pk>/", views.update_item, name="update_item"),
    path("deleteItem/<str:pk>/", views.delete_item, name="delete_item"),
    path("change_status/", views.changeStatus, name="change_status"),
    ]