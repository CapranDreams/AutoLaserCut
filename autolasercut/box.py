import svgwrite
from svgwrite import cm, mm 
from autolasercut.utils import get_collection, get_records, add_record, new_record

def makeBox(length, width, height, _name="test.svg"):
    name = _name
    if name[-4:] != ".svg":
        name = name + ".svg"
    db_path = "/static/toolpaths/" + name
    name = "autolasercut/static/toolpaths/" + name

    if length <= 0:
        length = 1
    if width <= 0:
        width = 1
    if height <= 0:
        height = 1

    _stroke = 3

    svg = svgwrite.Drawing(name, profile='tiny')
    svg.add(svgwrite.shapes.Rect(insert=(0,0), size=(width*mm, length*mm), rx=0, ry=0, fill='white', stroke='red', stroke_width=_stroke))
    svg.save()

    mycollection = get_collection('toolpaths', 'tp')
    newRecord = new_record(_name, "box", db_path)
    add_record(mycollection, newRecord)

    return name