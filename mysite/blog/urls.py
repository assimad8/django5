from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # post views
    path('',post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',post_detail,name='post_detail'),
]

