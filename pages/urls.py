from django.urls import path
from .views import HomePageView,ImageViewFactory,ImageViewNoDI, AboutPageView, ContactPageView,ProductIndexView, ProductShowView, ProductCreateView, ProductCreatedView, ProductListView, CartView, CartRemoveAllView
from .utils import ImageLocalStorage



urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("about/", AboutPageView.as_view(), name='about'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("products/create/", ProductCreateView.as_view(), name="form"),
    path("products/created/", ProductCreatedView.as_view(), name="product-created"),
    path("products/<str:id>/", ProductShowView.as_view(), name="show"),
    path("products/", ProductListView.as_view(), name="index"),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenotdi_index'),
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenotdi_save'),

    
]

