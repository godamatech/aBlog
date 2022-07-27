 
from .views import Home, Details, AddPost, UpdatePost, DeletePost
from django.urls import path


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-post/', AddPost.as_view(), name='add-post'),
    path('details/<int:pk>', Details.as_view(), name='details'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete-post'),
    path('edit/<int:pk>', UpdatePost.as_view(), name='update-post'),
]
