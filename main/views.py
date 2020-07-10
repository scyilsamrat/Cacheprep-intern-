from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
import datetime
from django.views.decorators.csrf import csrf_exempt
from main.models import Questions
curl = settings.CURRENT_URL
media_url=settings.MEDIA_URL

date = datetime.datetime.now().date()
today = date.today()
d2 = str(today.strftime("%d-%m-%Y"))


def Home(request):
	return render(request, "index.html")

def Insert_question(request):
    if request.method == "POST":
        hsncode = request.POST.get('hsn','')
        pname = request.POST.get('pname','')
        MRP = request.POST.get('mrp','')
        pro = product(hsncode=hsncode, pname=pname, MRP=MRP, rate=rate, cgst=cgst, sgst=sgst)
        pro.save()
        return render(request, "Insert_question.html",{'curl': curl,'output':'Added successfully'})
    else:
        return render(request, "Insert_question.html",{'curl': curl,'output':''})

def Update_question(request):
    if request.method == "PUT":
        name = request.POST.get('name','')
        add = request.POST.get('add','')
        pno = request.POST.get('pno','NULL')
        gst = request.POST.get('gst','')
        cust = Customer(name=name,add=add,pno=int(pno),gst=gst)
        cust.save()
        return render(request,"AddCustomer.html",{'curl': curl,'output':'Added successfully'})
    else:
        return render(request,"AddCustomer.html",{'curl': curl,'output':''})


        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def Show_question(request):
    out=product.objects.values('id','hsncode','pname','MRP','rate','cgst','sgst')
    count=len(out)
    return render(request, "showproduct.html", {'curl': curl, 'out': out,'count':count})
