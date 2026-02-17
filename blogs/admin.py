from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, ContactMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "reading_time",
        "views",
        "created_at",
        "updated_at",
        "image_tag",
    )
    list_filter = (
        "is_published",
        "categories",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "excerpt", "content")
    readonly_fields = ("views", "reading_time", "created_at", "updated_at", "image_tag")

    filter_horizontal = ("categories",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)

    def image_tag(self, obj):
        if obj.base_image:
            return format_html('<img src="{}" width="80" style="object-fit: cover;"/>', obj.base_image.url)
        return "-"
    image_tag.short_description = "Rasm"

    actions = ["make_published", "make_unpublished"]

    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f"{updated} ta post published qilindi")
    make_published.short_description = "Belgilangan postlarni publish qilish"

    def make_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f"{updated} ta post unpublish qilindi")
    make_unpublished.short_description = "Belgilangan postlarni unpublish qilish"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")

    actions = ["mark_as_read", "mark_as_unread"]

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} ta xabar “o‘qilgan” holatga o‘tkazildi")
    mark_as_read.short_description = "Belgilangan xabarlarni o‘qilgan qilish"

    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f"{updated} ta xabar “o‘qilmagan” holatga o‘tkazildi")
    mark_as_unread.short_description = "Belgilangan xabarlarni o‘qilmagan qilish"
