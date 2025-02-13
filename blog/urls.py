from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(), name='home'),
    path("drafts/", views.PostDraftListView.as_view(), name='drafts'),
    path("create-post/", views.PostCreateView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/publish', views.publish_post, name='post_publish'),
    path('<slug:slug>/delete', views.delete_post, name='post_delete'),
    path('<int:pk>/create_comment/', views.add_comment, name='add_comment'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
    path('comment/<int:comment_id>/approve/', views.approve_comment, name='approve_comment'),
     
]