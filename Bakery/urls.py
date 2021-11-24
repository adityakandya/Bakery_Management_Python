from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='Bakery-index'),
	path('orderhistory/', views.order_history, name='Bakery-order'),
	path('placeorder/', views.place_order, name='Bakery-placeorder'),
	path('cart/', views.cart, name='Bakery-managecart'),
	path('signup/', views.Signup.as_view(), name='Bakery-signup'),
	path('login/', views.Login.as_view(), name='Bakery-login'),
]