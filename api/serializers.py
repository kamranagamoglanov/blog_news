from rest_framework import serializers

from news.models import BlogNews


class BlogNewsSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BlogNews
        fields = (
            "id",
            "url",
            "blog_name",
            "post_by",
            "category",
            "title",
            "tags",
            "descriptions",
            "count_views",
            "hero_image",
            "blog_image",
            "created_at"

        )



class BlogSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BlogNews
        fields = (
            "id",
            "url",
             "blog_name",
            "post_by",
            "category",
            "title",
            "tags",
            "descriptions",
            "count_views",
            "hero_image",
            "blog_image",
            "created_at"

        )



class NewsSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = BlogNews
        fields = (
            "id",
            "url",
            "blog_name",
            "post_by",
            "category",
            "title",
            "tags",
            "descriptions",
            "count_views",
            "hero_image",
            "blog_image",
            "created_at",
        )



#         fields = (
#             "id",
#             "url",
#             "category",
#             "title",
#             "descriptions",
#         )
# #         # fields = (
# #         #     "id",
# #         #     "url",
# #         #     "descriptions"
# #         # )


