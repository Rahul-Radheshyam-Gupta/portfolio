from django.shortcuts import render,HttpResponse,redirect
from .models import Visitor,Project
# Create your views here.

def dashboard(request):
    clicked_on = 'dashboard'
    data = {
        'clicked_on':clicked_on
    }
    return render(request,'home/dashboard.html',data)


def contact(request):
    print("=== post data ",request.POST)
    clicked_on = 'contact'
    data = {
        'clicked_on':clicked_on    }
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

        return render(request,'home/success_message.html',{'name':name,'clicked_on':clicked_on})
    return render(request,'home/contact.html',data)


def about(request):
    clicked_on = 'about'
    data = {
        'clicked_on':clicked_on
    }
    return render(request,'home/about.html',data)
    


def project(request):
    project_list = Project.objects.all()
    clicked_on = 'project'

    data = {
        'projects':project_list,
        'clicked_on':clicked_on
    }
    return render(request,'home/project.html',data)
