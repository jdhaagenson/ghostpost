from django.shortcuts import render, reverse
from ghostpost_app.models import Post
from ghostpost_app.forms import NewPostForm
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string
import string


# Create your views here.
def home_view(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'homepage.html', {'posts': posts})


def popular_view(request):
    posts = Post.objects.all()
    # score = 0
    posts = sorted(posts, key=lambda p: p.score, reverse=True)
    return render(request, 'homepage.html', {'posts': posts})


def new_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data.get('is_boast'),
                content=data.get('content'),
                secret=get_random_string(6, string.ascii_lowercase)
            )
            post = Post.objects.get(content=data.get('content'))
            return render(request, 'newpost.html', {'form': form, 'post': post})
    form = NewPostForm()
    return render(request, 'newpost.html', {'form': form})


def boasts_view(request):
    posts = Post.objects.filter(is_boast=True).order_by('-date')
    return render(request, 'homepage.html', {'posts': posts})


def roasts_view(request):
    posts = Post.objects.filter(is_boast=False).order_by('-date')
    return render(request, 'homepage.html', {'posts': posts})


def upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# extra credit:
def secret_view(request, secret):
    post = Post.objects.get(secret=secret)
    return render(request, 'secret.html', {'post': post})


def delete(request, secret):
    Post.objects.get(secret=secret).delete()
    return HttpResponseRedirect(reverse('homepage'))


def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_details.html', {'post': post})


