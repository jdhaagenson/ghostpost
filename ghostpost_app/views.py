from django.shortcuts import render
from ghostpost_app.models import Post
from ghostpost_app.forms import NewPostForm


# Create your views here.
def home_view(request):
    posts = Post.objects.all().order_by('time_posted')
    return render(request, 'homepage.html', {'posts': posts})