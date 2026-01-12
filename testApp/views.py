from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


def index(request):
    memo = ""

    if request.method == "POST":
        memo = request.POST.get("memo", "")

    context = {
        "title": "こんにちは、Hayashitani",
        "message": "これはテンプレートを使ったテストページです。",
        "food_list": ["プリン", "焼肉", "寿司", "ヨーグルト", "パン"],
        "test_input": "<script>alert('ハッキング成功！');</script>",
        "memo": memo,
    }

    return render(request, "index.html", context)


# Postモデルの一覧を返す、API専用ビュー（←これはそのままでOK）
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
