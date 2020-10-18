from django.shortcuts import render,HttpResponse,redirect
from .models import Visitor,Project,MyCv
# Create your views here.
def get_cv():
    try:
        return MyCv.objects.first()
    except:
        return False

def dashboard(request):
    clicked_on = 'dashboard'
    cv = get_cv()
    data = {
        'clicked_on':clicked_on,
        'cv':cv
    }
    return render(request,'home/dashboard.html',data)


def contact(request):
    print("=== post data ",request.POST)
    clicked_on = 'contact'
    cv = get_cv()
    data = {
        'clicked_on':clicked_on,
        'cv':cv
    }
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

        return render(request,'home/success_message.html',{'name':name,'clicked_on':clicked_on,'cv':cv})
    return render(request,'home/contact.html',data)


def about(request):
    clicked_on = 'about'
    cv = get_cv()
    data = {
        'clicked_on':clicked_on,
        'cv':cv
    }
    return render(request,'home/about.html',data)
    


def project(request):
    project_list = Project.objects.all()
    clicked_on = 'project'
    cv = get_cv()
    data = {
        'projects':project_list,
        'clicked_on':clicked_on,
        'cv':cv
    }
    return render(request,'home/project.html',data)
