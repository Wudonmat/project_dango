from django.urls import path

from landing import views

app_name = "landing"
urlpatterns = [
    path("", views.landing_main, name="main"),
    # path("<int:blog_id>/", views.shop_blog_home, name="home"),
]
