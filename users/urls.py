from .views import RegisterApiView, LoginApiView, AuthUserApiView
from django.urls import path

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name="register"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('user/', AuthUserApiView.as_view(), name="user"),

]
