from django.shortcuts import render
def jingatag(request):
    d={'name':'anvitha','age':18}
    return render(request,'jingatag.html',context=d)

# Create your views here.
