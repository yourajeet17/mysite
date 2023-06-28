# this is the first page for starting the project
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Ajeet', 'place': 'Delhi'}
    return render(request, 'index.html', params)


def about(request):
    return HttpResponse("About")


def analyse(request):
    djtext = request.POST.get('userid', 'off')
    removepunc = request.POST.get('check1', 'off')
    fullcaps = request.POST.get('check2', 'off')
    print(removepunc)
    print(djtext)
    punctuation = ''',./?;:'"\|]}[{-_=+)(*&^%$#@!~'''
    analysed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analysed = analysed + char

        params = {'purpose': 'removed Punctuation', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif fullcaps == "on":
        for char in djtext:
            if char not in punctuation:
                analysed = analysed + char.upper()

        params = {'purpose': 'Text Changed into Upper case', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse("Error")
