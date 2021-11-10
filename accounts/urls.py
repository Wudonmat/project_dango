from django.urls import path
from accounts import views


app_name = "accounts"
urlpatterns = [
    path("sign-up/1/", views.sign_up_1, name="sign-up_1"),
    path("sign-up/2/", views.sign_up_2, name="sign-up_2"),
    path("sign-up/3/", views.sign_up_3, name="sign-up_3"),
    path("sign-up/4/", views.sign_up_4, name="sign-up_4"),
    path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),
    path("mypage/", views.user_profile, name="profile"),
    # path("mypage/<int:personal_id>/edit", views.user_profile_edit, name="profile_edit"),
]
