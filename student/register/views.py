from django.shortcuts import render,redirect
from .models import details
def home(request):
    return render(request,'home.html')

def insert(request):
    if request.method=='POST':
        fname=request.POST.get('studentfname')
        lname=request.POST.get('studentlname')
        number=request.POST.get('studentnumber')
        email=request.POST.get('studentemail')
        course=request.POST.get('studentcourse')
        address=request.POST.get('studentaddress')
        details.objects.create(studentfname=fname,studentlname=lname,studentnumber=number,
                               studentemail=email,studentcourse=course,studentaddress=address)
    return redirect('table')

def table(request):
    data=details.objects.all()
    return render(request,'table.html',{'allin':data})

def update(request,up):
    if request.method=='POST':
        edit=details.objects.get(id=up)
        edit.studentfname=request.POST.get('studentfname')
        edit.studentlname=request.POST.get('studentlname')
        edit.studentnumber=request.POST.get('studentnumber')
        edit.studentemail=request.POST.get('studentemail')
        edit.studentcourse=request.POST.get('studentcourse')
        edit.studentaddress=request.POST.get('studentaddress')
        edit.save()
        
    return redirect('table')

def updatepage(request,up):
    value=details.objects.get(id=up)
    return render(request,'update.html',{'newdata':value})

def delete(request,up):
    clear=details.objects.get(id=up).delete()
    return redirect('table')

def deletepage(request,up):
    erase=details.objects.get(id=up)
    return render(request,'delete.html',{'item':erase})
