from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    a = 3
    http_response = '' 
    content = f'''Hello, world. You're at the api index.<br>int a = {a}'''
    http_response += content
    content = ...
    http_response += content
    return HttpResponse(http_response)