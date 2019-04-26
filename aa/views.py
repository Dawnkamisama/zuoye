from django.shortcuts import render
from  . models import AA
from aa import pachong
from aa import models
# Create your views here.
def openbook(request):
    flag=0
    a=pachong.crow()
    ls=models.AA.objects.all()
    for i in ls :
        if(i.id==1):
            flag=1
            break
    if(flag==0):
        for i in range(len(a)):
            models.AA.objects.create(id=i,title=a[i])
    ls = models.AA.objects.all()

    return render(request,"wy.html",{'li':ls})