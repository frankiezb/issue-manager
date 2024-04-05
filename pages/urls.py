from django.urls import path 
from.views import HomePageView, AboutPageView, SignUpPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("signup/", SignUpPageView.as_view(), name="signup"),
]