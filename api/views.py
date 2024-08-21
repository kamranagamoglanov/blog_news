from .serializers import (
    BlogNewsSerializer,
    BlogSerializer,
    NewsSerializer,
)

from django.http import HttpRequest
from rest_framework import permissions, viewsets, mixins

from news.models import BlogNews, ViewCount


# class UpdateViewCountMixin(mixins.RetrieveModelMixin):
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.count_views += 1
#         instance.save(update_fields=['count_views'])
#         return super().retrieve(request, *args, **kwargs)
    


class UpdateViewCountMixin(viewsets.GenericViewSet):
    def retrieve(self, request: HttpRequest, *args, **kwargs):
        instance = self.get_object()
        ip_address = request.META.get('REMOTE_ADDR')

        view_count, created = ViewCount.objects.get_or_create(
            ip_address=ip_address,
            blog_news=instance
        )
        if created:
            instance.count_views += 1
            instance.save(update_fields=['count_views'])

        return super().retrieve(request, *args, **kwargs)


class BlogNewsViewSet(UpdateViewCountMixin ,viewsets.ModelViewSet):
    queryset = BlogNews.objects.all()
    serializer_class = BlogNewsSerializer


class BlogViewSet(UpdateViewCountMixin ,viewsets.ModelViewSet):
    queryset = BlogNews.objects.filter(category='BLOG')
    serializer_class = BlogSerializer


class NewsViewSet(UpdateViewCountMixin ,viewsets.ModelViewSet):
    queryset = BlogNews.objects.filter(category='NEWS')
    serializer_class = NewsSerializer






