from django.forms import ModelForm
from django import forms
#from .models import Toolpaths
from .models import *


class UploadForm(ModelForm):
    toolpath = forms.FileField()
    vectorlength = forms.FloatField(required=False)
    vectortype = forms.CharField(required=True, max_length=10)

    #class Meta:
    #    model = Toolpaths
    #    fields = ['toolpath', 'vectorlength', 'vectortype']

class BoxForm(forms.Form):
    box_Length = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Width = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Depth = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Name = forms.CharField(required=True, max_length=300, help_text="")

    class Meta:
        finally_fields = ['box_Length', 'box_Width', 'box_Depth', 'box_Name']
        
class BoxForm2(forms.Form):
    boxcode_Length = forms.IntegerField(required = False)
    boxcode_Width = forms.IntegerField(required = False)
    boxcode_Depth = forms.IntegerField(required = False)
    boxcode_Name = forms.CharField(required = True, empty_value="nameless box")
    boxcode_gcode = forms.CharField(widget=forms.Textarea(attrs={"rows":"30", "cols":"160", "id":"boxcode"}), required = False)

    class Meta:
        finally_fields = ['boxcode_Length', 'boxcode_Width', 'boxcode_Depth', 'boxcode_Name', 'boxcode_gcode']

class GearForm(forms.Form):
    gear_name = forms.CharField(required=True, max_length=300, help_text="")
    gear_teeth = forms.IntegerField(min_value=5, max_value=300, help_text="(mm)", required=True)
    gear_diameter = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)

    class Meta:
        finally_fields = ['gear_name', 'gear_teeth', 'gear_diameter']

class RasterForm(forms.Form):
    input_name = forms.CharField(max_length=300, help_text="")
    #binarization_threshold = forms.IntegerField(min_value=0, max_value=255, help_text="/255")
    #invert_image = forms.BooleanField(required=False)
    dither_or_recolor = forms.BooleanField(required=False)
    resolution = forms.IntegerField(min_value=16, max_value=4000)
    input_image = forms.FileField()

    class Meta:
        finally_fields = ['input_name', 'input_image']
        
class CutForm(forms.Form):
    input_name = forms.CharField(max_length=300, help_text="")
    lower_binarization_threshold = forms.IntegerField(min_value=0, max_value=255, help_text="/255")
    upper_binarization_threshold = forms.IntegerField(min_value=0, max_value=255, help_text="/255")
    invert_image = forms.BooleanField(required=False)
    input_image = forms.FileField()

    class Meta:
        finally_fields = ['input_name', 'input_image']