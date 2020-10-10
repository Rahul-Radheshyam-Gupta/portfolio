from django.shortcuts import render,HttpResponse,redirect
from .models import Visitor,Project
# Create your views here.
def dashboard(request):
    return render(request,'home/dashboard.html')


def contact(request):
    print("=== post data ",request.POST)
    if request.method == "POST":
        name = request.POST.get('uname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        role = request.POST.get('role')
        if role == 'on':
            role = True
        else:
            role = False
        visit = Visitor(name=name,
                email=email,
                mobile = mobile,
                message = message,
                hr = role
        )
        visit.save()

        return render(request,'home/success_message.html',{'name':name})
    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')
    


def project(request):
    project_list = Project.objects.all()
    return render(request,'home/project.html',{'projects':project_list})
