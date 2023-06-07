from django.urls import path, include
from blogging.views import PostListView, PostDetailView, PostDetailSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post_detail", PostDetailSet)
router.register(r"user_detail", UserViewSet)

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
