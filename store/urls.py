from django.conf.urls.static import static
from django.urls import path

from django_ecommerce import settings
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
#Adding media URL to URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)