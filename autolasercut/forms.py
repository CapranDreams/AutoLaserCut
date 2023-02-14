from django.forms import ModelForm
from django import forms
from .models import Toolpaths


class UploadForm(ModelForm):
    toolpath = forms.FileField()
    vectorlength = forms.FloatField(required=False)
    vectortype = forms.CharField(required=True, max_length=10)

    class Meta:
        model = Toolpaths
        fields = ['toolpath', 'vectorlength', 'vectortype']

class BoxForm(forms.Form):
    box_Length = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Width = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Depth = forms.IntegerField(min_value=1, max_value=100000, help_text="(mm)", required=True)
    box_Name = forms.CharField(required=True, max_length=300, help_text="(Name for this box)")

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