from django.urls import path
from . import views

urlpatterns=[
   path('', views.index, name='index'), 
]
from django.urls import path
from . import views
from .views import PostListAPIView   # ← これを追加！

urlpatterns = [
    path('', views.index, name='index'),

    # '/api/posts/' に来たら PostListAPIView を実行
    path("api/posts/", PostListAPIView.as_view(), name="post-list"),
]
