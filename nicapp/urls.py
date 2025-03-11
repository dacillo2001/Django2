from django.urls import path

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns=[
    path ('nicapp/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path ('nicapp/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
]