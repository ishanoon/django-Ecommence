from django.urls import path
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("checkout/", views.checkout, name="checkout"),
    path("cart/", views.cart, name="cart"),
    path("register/", views.UserCreation, name="register"),
    path("view_store/<str:pk>/", views.viewStore, name="view"),
    path("login/", views.UserLogin, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("user/", views.UserPage, name="user-page")
]
