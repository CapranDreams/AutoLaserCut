import svgwrite
from svgwrite import cm, mm 

box_width = 200
box_height = 100
box_position = (0*mm,0*mm)
box_radius = 0
_stroke = 3

dwg = svgwrite.Drawing('localtest/test.svg', profile='tiny')
#dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(100, 0, 0, '%')))
dwg.add(svgwrite.shapes.Rect(insert=box_position, size=(box_width*mm, box_height*mm), rx=box_radius, ry=box_radius, fill='white', stroke='red', stroke_width=_stroke))
#dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
#svgwrite.shapes.Polyline(points=[], **extra)
dwg.save()