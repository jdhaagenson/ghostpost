from django.shortcuts import render, reverse
from ghostpost_app.models import Post
from ghostpost_app.forms import NewPostForm
from datetime import datetime
from django.http import HttpResponseRedirect


# Create your views here.
def home_view(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'homepage.html', {'posts': posts})


def popular_view(request):
    posts = Post.objects.all()
    posts.order_by('-upvotes', 'downvotes')
    return render(request, 'homepage.html', {'posts': posts})


def new_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data.get('is_boast'),
                content=data.get('content'),
                date=datetime.now(),
                upvotes=0,
                downvotes=0
            )
            return HttpResponseRedirect(reverse("home_view"))
            # return HttpResponseRedirect(reverse("secret_view"))
    form = NewPostForm()
    return render(request, 'newpost.html', {'form': form})


def boasts_view(request):
    posts = Post.objects.filter(is_boast=True)
    return render(request, 'homepage.html', {'posts': posts})


def roasts_view(request):
    posts = Post.objects.filter(is_boast=False)
    return render(request, 'homepage.html', {'posts': posts})
