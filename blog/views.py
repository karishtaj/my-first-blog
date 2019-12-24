from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
# Create your views here.
def index(request):
	return render(request,"blog/index.html")

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})