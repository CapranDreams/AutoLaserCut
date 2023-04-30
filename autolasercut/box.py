import svgwrite
from svgwrite import cm, mm 
import math
from autolasercut.utils import get_collection, get_records, add_record, new_record
import tempfile, os

class Box:
    def makeBox(self, length, width, height, _name="test.svg"):
        name = _name
        if name[-4:] != ".svg":
            name = name + ".svg"
        db_path = "/static/toolpaths/" + name
        name = "autolasercut/autolasercut/static/toolpaths/" + name

        if length <= 0:
            length = 1
        if width <= 0:
            width = 1
        if height <= 0:
            height = 1

        _stroke = 1
        _depth = 10
        _padding = 10

        svg = svgwrite.Drawing(name, profile='tiny')

        # front
        leftOffset = height + _padding
        topOffset = height + _padding
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(length, width), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, width+topOffset, depth=_depth, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, length+leftOffset, depth=_depth, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        
        #back
        leftOffset = height + _padding + length + _padding + height + _padding 
        topOffset = height + _padding
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(length, width), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, width+topOffset, depth=_depth, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, length+leftOffset, depth=_depth, fingers=9), fill='white', stroke='red', stroke_width=_stroke))
        
        #bottom
        leftOffset = height + _padding
        topOffset = height + _padding + width + _padding
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(length, height), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=True, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, height+topOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, height+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=True, fingers=3), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, height+topOffset, length+leftOffset, depth=_depth, flipped=False, fingers=3), fill='white', stroke='red', stroke_width=_stroke))  #flipped

        #top
        leftOffset = height + _padding
        topOffset = 0
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(length, height), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=True, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, length+leftOffset, height+topOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, height+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=True, fingers=3), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, height+topOffset, length+leftOffset, depth=_depth, flipped=False, fingers=3), fill='white', stroke='red', stroke_width=_stroke))  #flipped

        #left
        leftOffset = 0
        topOffset = height + _padding
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(height, width), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, height+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=False, fingers=3), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, height+leftOffset, width+topOffset, depth=_depth, fingers=3), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=True, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, height+leftOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        
        #right
        leftOffset = height + _padding + length + _padding
        topOffset = height + _padding
        svg.add(svgwrite.shapes.Rect(insert=(leftOffset,topOffset), size=(height, width), rx=0, ry=0, fill='white', stroke='blue', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, height+leftOffset, 0+_depth+topOffset, depth=_depth, flipped=False, fingers=3), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeHorizontalJagLine(0+leftOffset, height+leftOffset, width+topOffset, depth=_depth, fingers=3), fill='white', stroke='red', stroke_width=_stroke))
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, 0+_depth+leftOffset, depth=_depth, flipped=True, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        svg.add(svgwrite.shapes.Polyline(points=self.makeVerticalJagLine(0+topOffset, width+topOffset, height+leftOffset, depth=_depth, flipped=False, fingers=9), fill='white', stroke='red', stroke_width=_stroke))  #flipped
        
        svg.save()

        mycollection = get_collection('toolpaths', 'tp')
        newRecord = new_record(_name, "box", db_path)
        add_record(mycollection, newRecord)

        return name


    def makeHorizontalJagLine(self, x0, x1, y0, depth=3, flipped=True, fingers=9):
        lengthOfLine = x1-x0
        polylines = []
        if(lengthOfLine <= depth):
            polylines= [(x0, y0),(x1, y0)]
            return polylines

        if fingers % 2 == 0:
            fingers = fingers+1

        y = flipped

        if flipped:
            polylines.append((x0, y0))
        else:
            polylines.append((x0, y0-depth))

        for x in range(1,fingers):    # divide into 9 segments (must be odd to end with same direction)
            if y:
                polylines.append(((x1-x0)*(x/fingers)+x0, y0))
                polylines.append(((x1-x0)*(x/fingers)+x0, y0-depth))
            else:
                polylines.append(((x1-x0)*(x/fingers)+x0, y0-depth))
                polylines.append(((x1-x0)*(x/fingers)+x0, y0))
            y = not y

        if flipped:
            polylines.append((x1, y0))
        else:
            polylines.append((x1, y0-depth))

        return polylines

    def makeVerticalJagLine(self, y0, y1, x0, depth=3, flipped=True, fingers=9):
        lengthOfLine = y1-y0
        polylines = []
        if(lengthOfLine <= depth):
            polylines= [(x0, y0),(x0, y1)]
            return polylines
        
        if fingers % 2 == 0:
            fingers = fingers+1

        x = flipped

        if flipped:
            polylines.append((x0, y0))
        else:
            polylines.append((x0-depth, y0))

        for y in range(1,fingers):    # divide into 9 segments (must be odd to end with same direction)
            if x:
                polylines.append((x0, (y1-y0)*(y/fingers)+y0))
                polylines.append((x0-depth, (y1-y0)*(y/fingers)+y0))
            else:
                polylines.append((x0-depth, (y1-y0)*(y/fingers)+y0))
                polylines.append((x0, (y1-y0)*(y/fingers)+y0))
            x = not x
            
        if flipped:
            polylines.append((x0, y1))
        else:
            polylines.append((x0-depth, y1))

        return polylines
