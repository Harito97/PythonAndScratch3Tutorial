from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Read the content from the file
    with open('/Data/HaritoWork/PythonAndScratch3Tutorial/Python/Khoa3_Web/clean_law_data.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    html_page = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luật Nuôi con nuôi</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 800px;
            padding: 20px;
        }}
        h1, h2 {{
            text-align: center;
        }}
        .center {{
            text-align: center;
        }}
    </style>
</head>
<body>
    {content}
</body>
</html>
    """
    return HttpResponse(html_page)
    # return render(request, 'web_covid.html')
    # return HttpResponse("Hello, world. You're at the trang chu index.")