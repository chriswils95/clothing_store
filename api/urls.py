from typing import ItemsView
from django.urls import path
from .views import CreateItemsView, ItemView

urlpatterns = [
    path('items', ItemView.as_view()),
    path("create-item", CreateItemsView.as_view())
]
