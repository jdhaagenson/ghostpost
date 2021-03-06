"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ghostpost_app.views import new_post_view, home_view, \
    boasts_view, roasts_view, popular_view, upvote, downvote

urlpatterns = [
    path('', home_view, name="homepage"),
    path('new/', new_post_view, name="newpost"),
    path('roasts/', roasts_view, name='roasts'),
    path('boasts/', boasts_view, name='boasts'),
    path('popular/', popular_view, name="popular"),
    path('upvote/<int:post_id>', upvote),
    path('downvote/<int:post_id>', downvote),
    path('admin/', admin.site.urls),
]
