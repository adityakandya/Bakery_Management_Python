from django.urls import path
from Bakery.Views import views, login, signup, cart,checkout

urlpatterns = [
	path('', views.Index.as_view(), name='Bakery-index'),
	path('orderhistory/', views.order_history.as_view(), name='Bakery-order'),
	path('placeorder/', views.place_order, name='Bakery-placeorder'),
	path('cart/', cart.Cart.as_view(), name='Bakery-cart'),
	path('signup/', signup.Signup.as_view(), name='Bakery-signup'),
	path('login/', login.Login.as_view(), name='Bakery-login'),
	path('logout/', views.logout, name='Bakery-logout'),
	path('check-out/', checkout.Checkout.as_view(), name='Bakery-checkout'),
	path('profile/', views.profile.as_view(), name='Bakery-profile'),

]
