from django.urls import path
from Bakery.Views import views, login, signup

urlpatterns = [
	path('', views.index, name='Bakery-index'),
	path('orderhistory/', views.order_history, name='Bakery-order'),
	path('placeorder/', views.place_order, name='Bakery-placeorder'),
	path('cart/', views.cart, name='Bakery-managecart'),
	path('signup/', signup.Signup.as_view(), name='Bakery-signup'),
	path('login/', login.Login.as_view(), name='Bakery-login'),
]