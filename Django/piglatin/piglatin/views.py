from django.http import HttpResponse
from django.shortcuts import render

#to run the server do "python manage.py runserver"

def home(request):
    return render(request, 'home.html')

def translate(request):
    #getting the information is in the request callback
    original = request.GET['originaltext'].lower()
    translation = ''

    for word in original.split():
        if word[0] in ['a','e','i','o','u']:
            #is vowel
            translation += word
            translation += 'yay '
        else:
            #is consonant
            translation += word[1:]
            translation += word[0]
            translation += 'ay '
    items_to_send = {'original': original, 'translation': translation}
    return render(request, 'translate.html', items_to_send)

def about(request):
    return render(request, 'about.html')

