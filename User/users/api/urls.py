from django.urls import path
from users.api.views import (
    UserRegistrationView,
    GetUserDetailsView,
    PhoneLoginView

)
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', UserRegistrationView.as_view(),name="user-register"),
    path('login/', PhoneLoginView.as_view(), name='phone-login'),
    path('user/details/', GetUserDetailsView.as_view(), name='get_user_details'),

]