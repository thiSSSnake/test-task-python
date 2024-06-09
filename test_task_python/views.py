from django.shortcuts import render


def home_view(request):
    '''Just simple view func thath returns a home page.'''
    return render(request, 'home.html')
