from django.shortcuts import render
from django.http import HttpResponse
from .templates.web_gia_vang import HTML_FORM

# Create your views here.
def index(request):
    # Eg1:
    # a = 3
    # http_response = ''
    # content = f'''Hello, world. You're at the api index.<br>int a = {a}'''
    # http_response += content
    # content = ...
    # http_response += content

    # Eg2:
    http_response = '' + HTML_FORM

    return HttpResponse(http_response)

