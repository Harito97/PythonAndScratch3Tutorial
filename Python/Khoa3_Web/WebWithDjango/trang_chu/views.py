from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ...
    # return HttpResponse("Hello, world. You're at the trang chu index.")
    # return render(request, 'web_covid.html')
    return HttpResponse(html_page)
