from django.http import HttpResponse

def aboutUs_view(request):
    return HttpResponse("This is the About Us page.")