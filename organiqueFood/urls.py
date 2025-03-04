from django.urls import path
from . import views as organique_views

urlpatterns = [
    path("", organique_views.index, name="index"),
    path("products/", organique_views.AllProducts, name="all-product"),
    path("view-product/<str:pk>", organique_views.ProductViewer, name="view-product"),
    path('filters/<str:pk>', organique_views.ByCategory, name="by-category"),
    path("like/<str:pk>", organique_views.AddItem, name="add"),
]