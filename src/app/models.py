from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField(max_length=20000, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=title, verbose_name="Date Published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    authod = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, unique=True)

    def __str__(self):
        return self.title
