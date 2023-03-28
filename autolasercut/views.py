from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import svgwrite
from svgwrite import cm, mm 
from autolasercut.utils import get_collection, get_records, add_record, new_record
from autolasercut.box import makeBox
from autolasercut.gears import makeGear

def home_view(request):
    return render(request, 'index.html', {'name':'wololololo'})

def cut_view(request):
    return render(request, 'cut.html', {'name':'cut_view'})

def raster_view(request):
    return render(request, 'raster.html', {'name':'raster_view'})

def box_view(request):
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            boxName = cd.get('box_Name')
            boxDims = [cd.get('box_Length'), cd.get('box_Width'), cd.get('box_Depth')]
            myBox = makeBox(boxDims[0], boxDims[1], boxDims[2], boxName)
            print(myBox)
        else:
            print(form.errors)

    return render(request, 'box.html', {'form':BoxForm})


def gear_view(request):
    if request.method == 'POST':
        form = GearForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            gear_name = cd.get('gear_name')
            gear_teeth = cd.get('gear_teeth')
            gear_diameter = cd.get('gear_diameter')
            myGear = makeGear(gear_name, gear_teeth, gear_diameter, side=0)
        else:
            print(form.errors)

    return render(request, 'gear.html', {'form':GearForm})

def db_view(request):
    mycollection = get_collection('toolpaths', 'tp')

    rows = get_records(mycollection)

    return render(request, 'db.html', {'data':rows})

'''
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

    return render(request, 'db_upload.html', {'data':toolpaths, 'form':UploadForm})
'''



