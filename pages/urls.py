from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView, ProductListView
urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("products/create/", ProductCreateView.as_view(), name="form"),
    path("products/created/", ProductCreatedView.as_view(), name="product-created"),
    path("products/<str:id>/", ProductShowView.as_view(), name="show"),
    path("products/", ProductListView.as_view(), name="index"),
    
]