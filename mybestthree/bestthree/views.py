from django.shortcuts import render

# Create your views here.

context = {
    'mainTitle': 'Best Three Real Estate Agents',
}


def home(request):
    return render(request, 'base.html', context)
