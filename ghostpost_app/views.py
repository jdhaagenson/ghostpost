import string, random
from django.shortcuts import render, reverse
from ghostpost_app.models import Post
from ghostpost_app.forms import NewPostForm
from django.http import HttpResponseRedirect


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
                content=data.get('content')
            )
            return HttpResponseRedirect(reverse("homepage"))
            # return HttpResponseRedirect(reverse("secret_view"))
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
    return HttpResponseRedirect(reverse(request.META.get('HTTP_REFERER')))


def downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse(request.META.get('HTTP_REFERER')))


# extra credit:
def secret_view(request, post_id):
    letters = string.ascii_lowercase
    post = Post.objects.get(post_id)
    secret = ''.join(random.choice(letters) for i in range(6))

