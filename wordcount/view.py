from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request,'home.html')
# def contact(request):
#     return render(request,"contact.html")
def count(request):
    data=request.GET.get('fulltext')
    words=str(data).split(" ")
    counted_words={}
    for x in words:
           if x in counted_words:
               counted_words[x]=counted_words[x]+1
           else:
                counted_words[x]=1
    total_words=len(words)
    return render(request,"count.html",{'total_words':total_words,'counted_words':counted_words.items()})
# def startwiths(request):
#     info=request.GET['fulltext']
#     print(info)
#     words=str(info).split(" ")
#     start_with_s=[x for x in words if x.startswith('s')]
#     alphabetWiths=len(start_with_s)
#     return render(request,'startWiths.html',{'alphabetWiths':alphabetWiths,
#              'start_with_s':start_with_s})
def aboutus(request):
    return render(request,"aboutus.html")
