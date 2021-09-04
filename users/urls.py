from django.urls import path
from knox import views as Knox_views
from users.views import (RegisterAPIView, LoginAPIView,EmailActivationAPIView, ProfileAPIView)
from django.views.generic import TemplateView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', Knox_views.LogoutView.as_view()),
    path('profile/',ProfileAPIView.as_view(),name='profile'),
    path('logoutall/', Knox_views.LogoutAllView.as_view()),
    path('activation/<str:uidb64>/<str:token>/',EmailActivationAPIView.as_view(),name='activate'),
]
