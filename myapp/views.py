from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    data ={
        'title': 'Home Page',
        'content': 'Welcome to the Home Page',
        'clist': ['Python', 'Django', 'JavaScript', 'HTML', 'CSS']
    }
    return render(request, 'index.html',data)

def aboutUs_view(request):
    return HttpResponse("This is the About Us page.")

def cources_view(request):
    return HttpResponse("This is the Courses page.")

def courcesDetails(request,courseid):
    return HttpResponse(f"This is the Courses page {courseid}.")
