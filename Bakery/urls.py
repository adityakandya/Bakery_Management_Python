from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='Bakery-index'),
	path('orderhistory/', views.order_history, name='Bakery-order'),
	path('placeorder/', views.place_order, name='Bakery-placeorder'),
	path('cart/', views.cart, name='Bakery-managecart'),
]