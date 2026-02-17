from django.urls import path
from .views import HomePageView, PostListView, PostDetailView, CategoryPostListView, ContactView, TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<int:category_id>/', CategoryPostListView.as_view(), name='category_posts'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
]
