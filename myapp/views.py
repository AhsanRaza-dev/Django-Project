from django.http import HttpResponse

def aboutUs_view(request):
    return HttpResponse("This is the About Us page.")

def cources_view(request):
    return HttpResponse("This is the Courses page.")

def courcesDetails(request,courseid):
    return HttpResponse(f"This is the Courses page {courseid}.")