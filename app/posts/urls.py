from django.urls import path

from posts.apis import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListCreateGenericAPIView.as_view(), name='list_create'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyGenericAPIView.as_view(),
         name='retrieve_update_destroy'),
    path('<int:pk>/like/', views.PostLikeToggleAPIView.as_view(),
         name='like'),
    path('<int:pk>/comment/', views.PostCommentListCreateGenericAPIView.as_view(),
         name='comment'),
    path('<int:post_pk>/comment/<int:pk>/',
         views.PostCommentUpdateDestroyGenericAPIView.as_view(),
         name='comment_update_delete'),
    path('category/', views.PostCategoryListGenericAPIView.as_view(), name='category'),
]
