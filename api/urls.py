from typing import ItemsView
from django.urls import path
from .views import CreateItemsView, ItemView, DeleteView

urlpatterns = [
    path('items', ItemView.as_view()),
    path("create-item", CreateItemsView.as_view()),
    path("delete-all-items",  DeleteView.as_view())
]
