from django.urls import path, include

from rest_framework import routers

from .views import (
    BlogNewsViewSet,
    BlogViewSet,
    NewsViewSet,
)



router = routers.DefaultRouter()
router.register(r'blog_news/filter=blogs', BlogViewSet, basename='blog')
router.register(r'blog_news/filter=news', NewsViewSet, basename='news')
router.register(r'blog_news', BlogNewsViewSet, basename='blognews')




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]