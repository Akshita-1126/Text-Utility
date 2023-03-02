from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
#    return HttpResponse('<h1> Personal Navigator </h1> <a href="#"> Google </a> <br> <a href="#"> Instagram </a> <br>')

def analyze(request):
    djtext= request.GET.get('text','default')
    removepunc= request.GET.get('removepunc','off')
    fullcaps= request.GET.get('fullcaps','off')
    newlinerem= request.GET.get('newlinerem','off')
    spacerem= request.GET.get('spacerem','off')
    countchar= request.GET.get('countchar','off')
    # Remove Punctuation
    if removepunc== 'on':
        punctuation=''',.;'"!?/:\%<>'''
        analyze= ""
        for char in djtext:
            if char not in punctuation:
                analyze= analyze+char

        params= {'purpose':'Remove Punctuation','analyzed_text':analyze}
        return render(request, 'analyzed.html', params)
    
    #Full capitals
    elif(fullcaps=='on'):
        analyze=""
        for char in djtext:
            analyze= analyze+ char.upper()
        params= {'purpose':'change to UPPERCASE','analyzed_text':analyze}
        return render(request, 'analyzed.html', params)

    #New Line Remover
    elif(newlinerem=='on'):
        analyze=""
        for char in djtext:
            if char !='\n':
                analyze= analyze+char
        params= {'purpose':'New Line Remover','analyzed_text':analyze}
        return render(request, 'analyzed.html', params)

    # space Remover
    elif(spacerem=='on'):
        analyze=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]== " "):
                analyze=analyze+char
        params= {'purpose':'Space Remover','analyzed_text':analyze}
        return render(request, 'analyzed.html', params)
    
    # Character count
    elif(countchar=='on'):
        c=0
        for char in djtext:
            if char!=' ':
                c=c+1
        analyze= 'The character count is '+ str(c)
        params= {'purpose':'Space Remover','analyzed_text':analyze}
        return render(request, 'analyzed.html', params)
    # For other
    else:
        return HttpResponse('Error')