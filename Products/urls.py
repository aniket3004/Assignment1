from django.urls import path
from Products import views

urlpatterns = [
    path('product/',views.ProductsView),
]
