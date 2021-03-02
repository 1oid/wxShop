from django.urls import path

from app.views_.ProductView import ProductListView

urlpatterns = [
    path("products", ProductListView.as_view({
        "get": "list"
    }))
]
