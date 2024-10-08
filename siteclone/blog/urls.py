from blog import views
from django.urls import path, re_path
from .views import AddCommentToPost
from .views import CommentApprovedView


# urls.py
from .views import CommentRemoveView
from .views import PostPublishView





urlpatterns = [


    path('', views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/', views.DraftListView.as_view(),name='post_draft_list'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post.as_view(),name='add_comment_to_post'),
    path('post/<int:pk>/comment/', AddCommentToPost.as_view(), name='add_comment_to_post'),
    # path('comment/<int:pk>/approve/', views.comment_approved, name='comment_approve'),
    path('comment/<int:pk>/approve/', CommentApprovedView.as_view(), name='comment_approve'),
    # path('comment/<int:pk>/remove/', views.comment_remove.as_view(),name='comment_remove'),
    path('comment/<int:pk>/remove/', CommentRemoveView.as_view(), name='comment_remove'),
    # path('post/<int:pk>/publish/', views.post_publish.as_view(),name='post_publish'),
    path('post/<int:pk>/publish/', PostPublishView.as_view(), name='post_publish'),
 

]

