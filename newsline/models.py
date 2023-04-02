from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    comment = models.CharField(max_length=1000)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos/")
    description = models.TextField()
    comment = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
