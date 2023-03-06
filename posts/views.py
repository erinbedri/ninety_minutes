from django.views.generic import ListView, DetailView

from posts.models import Post


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2


class PostDetails(DetailView):
    model = Post
    context_object_name = "post"
