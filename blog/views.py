from django.shortcuts import render
from blog.views import index

# Create your views here.
def index(request):
	return render(request,blog/index.html)