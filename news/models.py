from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
# from ckeditor.fields import RichTextField



class BlogNews(models.Model):
    CONTENT = (
    ("BLOG", "Blog"),
    ("NEWS", "News"),
    )
    category = models.CharField("Content", max_length=4, choices=CONTENT, null=False)
    blog_name = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=1000, null= False)
    descriptions = CKEditor5Field(max_length=30000,blank=False,null=False)
    tags = CKEditor5Field(max_length=30000,blank=False,null=False)
    # descriptions = RichTextField(max_length=30000,blank=False,null=False)
    count_views = models.PositiveIntegerField(default=0) 
    post_by = models.CharField(max_length=64, null=False)
    hero_image = models.FileField(upload_to="images/hero/%y/%m/%d/")
    blog_image = models.FileField(upload_to="images/blog/%y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Category:{self.category} --> Blog Name:{self.blog_name}"

    class Meta:
        verbose_name_plural = "Blog-News"
        verbose_name= "Blog News"


    
class ViewCount(models.Model):
    ip_address = models.GenericIPAddressField()
    blog_news = models.ForeignKey(BlogNews, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

