from django.urls import path

from matching import views

app_name = "matching"
urlpatterns = [
    path("", views.matching_main, name="main"),
    path("request/", views.request_list, name="request"),
    # path("<int:area_id>/", views.matching_area, name="main"),
    # path("<int:area_id>/<int:user_id>/list", views.matching_main, name="main"),
    # path("<int:blog_id>/", views.shop_blog_home, name="home"),
]