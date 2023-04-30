from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import svgwrite
from svgwrite import cm, mm 
from autolasercut.utils import *
from autolasercut.box import *
from autolasercut.gears import *
from autolasercut.vision import *

def home_view(request):
    return render(request, 'index.html', {'name':'wololololo'})

def cut_view(request):
    img_path = ""
    out_img = ""

    if request.method == 'POST':
        form = CutForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            input_name = cd.get('input_name')           
            bin_thresh = cd.get('lower_binarization_threshold') 
            bin_thresh2 = cd.get('upper_binarization_threshold')   
            inv_img = cd.get('invert_image')      

            new_vision = Vision()
            img_path = new_vision.handle_uploaded_file(request.FILES["input_image"], input_name)
            out_img = new_vision.trace_img(input_name, img_path, bin_thresh, bin_thresh2, inv_img)
            
        else:
            print(form.errors)

    return render(request, 'cut.html', {'form':CutForm, 'srcimg':img_path, 'outimg':out_img})

def raster_view(request):
    img_path = ""
    out_img = ""

    if request.method == 'POST':
        form = RasterForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            input_name = cd.get('input_name')           
            dither_or_recolor = cd.get('dither_or_recolor')   
            resolution = cd.get('resolution')

            new_vision = Vision()
            img_path = new_vision.handle_uploaded_file(request.FILES["input_image"], input_name)
            out_img = new_vision.dither_img(input_name, img_path, dither_or_recolor, resolution)
            
            
        else:
            print(form.errors)

    return render(request, 'raster.html', {'form':RasterForm, 'srcimg':img_path, 'outimg':out_img})

def box_view(request):
    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            boxName = cd.get('box_Name')
            boxDims = [cd.get('box_Length'), cd.get('box_Width'), cd.get('box_Depth')]

            new_box = Box()
            myBox = new_box.makeBox(boxDims[0], boxDims[1], boxDims[2], boxName)
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

            new_gear = Gear()
            myGear = new_gear.makeGear(gear_name, gear_teeth, gear_diameter, side=0)
        else:
            print(form.errors)

    return render(request, 'gear.html', {'form':GearForm})

def db_view(request):
    mycollection = get_collection('toolpaths', 'tp')

    rows = get_records(mycollection)

    return render(request, 'db.html', {'data':rows})


