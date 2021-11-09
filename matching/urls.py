from django.urls import path

from matching import views

app_name = "matching"
urlpatterns = [
    path("", views.matching_main, name="main"),
    # path("<int:blog_id>/", views.shop_blog_home, name="home"),
]