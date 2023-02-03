from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list'


class PostCreate(LoginRequiredMixin, generic.CreateView):

    model = Post
    fields = ['title', 'slug', 'author', 'content', 'image']
    success_url = reverse_lazy('post_list')
    template_name = "post/post_create.html"


class PostUpdate(LoginRequiredMixin, generic.UpdateView):

    model = Post
    fields = ['title', 'slug', 'author', 'content', 'image']
    success_url = reverse_lazy('post_list')
    template_name = "post/post_create.html"


class PostDelete(LoginRequiredMixin, generic.DeleteView):

    model = Post
    success_url = reverse_lazy('post_list')
    template_name = "post/post_delete.html"


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request, 
        template_name='post/post_detail.html',
        context={'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form}
        )
