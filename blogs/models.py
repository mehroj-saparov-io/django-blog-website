from django.db import models
from django.utils.text import slugify
import math


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    categories = models.ManyToManyField(
        Category,
        related_name="posts",
        blank=True
    )

    base_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
        help_text="Post uchun asosiy rasm"
    )

    excerpt = models.TextField(max_length=300, blank=True)
    content = models.TextField()

    reading_time = models.PositiveIntegerField(default=1)
    views = models.PositiveIntegerField(default=0)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["views"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            i = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{i}"
                i += 1
            self.slug = slug

        if self.content:
            words = len(self.content.split())
            self.reading_time = max(1, math.ceil(words / 180))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
