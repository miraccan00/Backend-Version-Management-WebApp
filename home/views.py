from django.shortcuts import render,redirect
from django.shortcuts import render
from .models import ReleaseProject1

def home(request):
    return render(request,'home/index.html')

def projectname1(request):
    releases = ReleaseProject1.objects.all()
    print(releases)
    context= {
        'releases':releases
    }
    return render(request,'home/projectname1.html',context)

def projectname2(request):
    return render(request,'home/projectname2.html')

def projectform1(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        release_artifact = request.POST.get('release_artifact')
        release_number = request.POST.get('release_number')
        release_path = request.POST.get('release_path')
        service_name = request.POST.get('service_name')
        version = request.POST.get('version')
        microui = bool(request.POST.get('microui'))
        sql = bool(request.POST.get('sql'))
        uat = bool(request.POST.get('uat'))
        prod = bool(request.POST.get('prod'))
        print(date) 
        print(microui)
        print(prod)
        projectform1 = ReleaseProject1(date=date,release_artifact=release_artifact,release_number=release_number,release_path=release_path,service_name=service_name,version=version,microui=microui,sql=sql,uat=uat,prod=prod)
        projectform1.save()
        return redirect('home:projectname1')
    return render(request,'home/project1form.html')