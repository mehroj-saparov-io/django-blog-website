from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.db.models import F, Q
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Category, ContactMessage
from django.utils.translation import gettext as _

# ------------------------------
# Home Page
# ------------------------------
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Oxirgi 3 ta post
        context['latest_posts'] = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
        # About me info
        context['about_me'] = {
            "name": _("Mehroj Saparov"),
            "bio": _("Python Backend Developer and Financial Specialist"),
            "resume_link": "/static/Mehroj_Saparov_Resume.pdf"
        }
        return context

# ------------------------------
# Post List (search + category filter + pagination)
# ------------------------------
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        qs = Post.objects.filter(is_published=True).order_by('-created_at')
        
        # Category filter
        category_id = self.request.GET.get('category')
        if category_id:
            qs = qs.filter(categories__id=category_id)
        
        # Search qidiruv
        search_query = self.request.GET.get('q')
        if search_query:
            qs = qs.filter(
                Q(title__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(content__icontains=search_query)
            ).distinct()
        
        return qs

    def get_paginate_by(self, queryset):
        limit = self.request.GET.get('limit')
        if limit and limit.isdigit():
            return int(limit)
        return self.paginate_by

# ------------------------------
# Post Detail + views count
# ------------------------------
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "post"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Views count oshirish
        Post.objects.filter(id=obj.id).update(views=F("views") + 1)
        obj.refresh_from_db()
        return obj

# ------------------------------
# Category posts
# ------------------------------
class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        category = get_object_or_404(Category, id=category_id)
        return category.posts.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactView(CreateView):
    model = ContactMessage
    template_name = "contact.html"
    fields = ["name", "email", "subject", "message"]
    success_url = "/"  # yoki reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ph_name']    = _("Ismingizni kiriting")
        context['ph_email']   = _("Email manzilingiz")
        context['ph_subject'] = _("Mavzu yozing")
        context['ph_message'] = _("Xabaringizni bu yerga yozing...")
        
        return context