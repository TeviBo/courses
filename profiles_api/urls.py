from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")

# No necesitamos establecer un nombre porque Django lo resuelve tomando el del modelo
router.register("profile", views.UserProfileViewSet)

router.register("feed", views.UserProfileFeedViewSet)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
