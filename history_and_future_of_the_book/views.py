from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Table

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'history_and_future_of_the_book/post_list.html', {'posts': posts})

def index(request):
	tables = Table.objects.filter(file_position='dfghjk')
	return render(request, 'history_and_future_of_the_book/index.html', {'tables':tables})
