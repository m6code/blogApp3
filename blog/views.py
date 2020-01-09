from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Benjamz',
		'title': 'Blog 1',
		'content': 'First Post content',
		'date_posted': 'January 9, 2020'
	},

	{
		'author': 'Benjamz',
		'title': 'Blog 2',
		'content': 'Second Post content',
		'date_posted': 'January 9, 2020'
	},
	{
		'author': 'Benjamz',
		'title': 'Blog 3',
		'content': 'Third Post content',
		'date_posted': 'January 9, 2020'
	},

]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, "blog/home.html", context)

def about(request):
	return render(request, 'blog/about.html', title="About Page")