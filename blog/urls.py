from .views import *
from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>/', Post_detail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', Tag_detail.as_view(), name='tag_detail_url')

]