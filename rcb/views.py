from django.shortcuts import render
def jingatag2(request):
    d={'name':'shinchan','age':20}
    return render(request,'jingatag.html',context=d)

# Create your views here.
