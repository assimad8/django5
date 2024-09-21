from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # post views
    path('',post_list,name='post_list'),
    path('<int:id>/',post_detail,name='post_detail'),
]

