from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html',context={'a':10,'b':15,'c':20})

def for1(request):
    return render(request,'for1.html',context={'name':'madan'})