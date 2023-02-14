from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home_view(request):
    return render(request, 'index.html', {'name':'wololololo'})

def cut_view(request):
    return render(request, 'cut.html', {'name':'cut_view'})

def raster_view(request):
    return render(request, 'raster.html', {'name':'raster_view'})

def box_view(request):
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)
        form2 = BoxForm2(request.POST, request.FILES)
        if form2.is_valid():
            cd = form2.cleaned_data
            boxName = cd.get('boxcode_Name') + ".gcode"
            boxDims = [cd.get('boxcode_Length'), cd.get('boxcode_Width'), cd.get('boxcode_Depth')]
            #do something with gcode...
            newTP = Toolpaths(toolpath=boxName ,vectorlength=boxDims[0]+boxDims[1]+boxDims[2], vectortype="box")
            newTP.save()
            print(newTP)
        else:
            print(form2.errors)

            
    return render(request, 'box.html', {'form':BoxForm, 'form2':BoxForm2})


def gear_view(request):
    return render(request, 'gear.html', {'name':'gear_view'})

def db_view(request):
    toolpaths = Toolpaths.objects.all()
    return render(request, 'db.html', {'data':toolpaths})

def db_upload(request):
    toolpaths = Toolpaths.objects.all()
    if request.method == 'POST' and request.FILES['toolpath']:
        form = UploadForm(request.POST, request.FILES)
        #print(request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            
            fs = FileSystemStorage()
            myfile = request.FILES['toolpath']
            filename = fs.save("autolasercut/toolpaths/"+myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)

    #return render(request, 'db_upload.html', {'data':toolpaths, 'form':form})
    return render(request, 'db_upload.html', {'data':toolpaths, 'form':UploadForm})
