from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
	try:
		posts_list = paginator.page(page)
	except PageNotAnInteger:
		posts_list = paginator.page(1)
	except EmptyPage:
		posts_list = paginator.page(paginator.num_pages)

	return render(request, 'post/index.html', {'page': page, 'posts': posts_list})


def post_details(request, post_id):
	current_post = Post.objects.get(pk=post_id)
	tags = current_post.tags.all()

	return render(request, 'post/post_details.html', {'current_post': current_post,
		'tags': tags})
