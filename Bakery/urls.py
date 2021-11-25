from django.urls import path
from Bakery.Views import views, login, signup, cart,checkout, pass_reset, editprofile, changepassword

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
	path('editprofile/', views.editprofile.as_view(), name='Bakery-editprofile'),
	path('password_reset/', pass_reset.PasswordReset.as_view(), name='password_reset'),
	path('password_reset_check/', pass_reset.PasswordResetCheck.as_view(), name='password_reset_check'),
	path('verify_user/', pass_reset.VerifyUser.as_view(), name='verify_user'),
	path('verify_check/', pass_reset.VerifyCheck.as_view(), name='verify_check'),
	path('edit_profile/', editprofile.EditProfile.as_view(), name = 'Bakery-editprofile'),
	path('change_password/', changepassword.ChangePassword.as_view(), name = 'Bakery-changepassword'),

]
