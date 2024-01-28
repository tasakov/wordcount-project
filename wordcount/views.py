from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()

    worddict={}
    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word]+=1
        else:
            #add to the dict
            worddict[word]=1
    sortedWords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})

def about(request):
    return render(request,'about.html')