from django.shortcuts import render
from blog.models import Post
# Create your views here.
def index(request):
	return render(request,"blog/index.html")

def post_list(request):
    return render(request, 'blog/post_list.html', {})