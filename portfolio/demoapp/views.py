from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact



# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')


def resume(request):
    return render(request,'resume.html')

def about(request):
    return render(request,'about.html')

def hire(request):
    submitted = False
 
    if request.method=='POST':
        company_name=request.POST.get('companyn')
        recruiter_name=request.POST.get('recruitern')
        description=request.POST.get('description')
        recruiter_email=request.POST.get('emailrecruiter')
        
        Contact.objects.create(company_name=company_name,recruiter_name=recruiter_name,description=description,recruiter_email=recruiter_email)
        submitted = True
    return render(request,'hire.html', {'submitted': submitted})

        

def hiresuccess(request):
    return render(request,'hiresuccess.html')