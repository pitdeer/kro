from django.shortcuts import render, render_to_response, HttpResponse
from basic_app.models import Category, Post

def index(request):
	posts = Post.objects.all().order_by('-date')[:10]
	context = { 'posts' : posts }
	return render_to_response('index.html',  context)

def category(request, id):
	category = Category.objects.filter(id=id) 
	return HttpResponse(category)

def all_categories(request):
	all_categories = Category.objects.all()
	return HttpResponse(all_categories)

def posts(request):
	posts = Post.objects.all()[:10]
	context = { 'posts' : posts }
	return render_to_response('category.html', context)
	