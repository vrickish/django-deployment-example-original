from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict= {'text': 'hello Vic', 'numbers':300}
    return render(request, 'tempApp/index.html', context_dict)

def about(request):
    return render(request, 'tempApp/about.html')

def relative(request):
    return render(request, 'tempApp/relative_url.html')