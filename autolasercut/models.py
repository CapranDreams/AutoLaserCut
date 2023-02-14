from django.db import models

class Toolpaths(models.Model):
    toolpath = models.FileField(upload_to='toolpaths')
    filename = models.FilePathField(path='toolpaths')
    vectorlength = models.FloatField(default=0.0)
    vectortype = models.CharField(max_length=10)
    #moddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.filename} is {self.vectorlength} lines long"
