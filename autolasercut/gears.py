import svgwrite
from svgwrite import cm, mm 
from autolasercut.utils import *
import numpy as np

import autolasercut.geometry.gear as gear


class Gear:
    def makeGear(self, _name, _teeth, diameter, pressureAngle=12, toothWidth=0.25, backlash=0.1, side=0):
        name = _name
        if name[-4:] != ".svg":
            name = name + ".svg"
        db_path = "/static/toolpaths/" + name
        name = "autolasercut/autolasercut/static/toolpaths/" + name

        mycollection = get_collection('toolpaths', 'tp')
        newRecord = new_record(_name, "gear", db_path)

        if side == 0: # spur gear
            pitch = 48
            teeth = _teeth
            pressure_angle = pressureAngle

            g = gear.Gear(pitch, teeth, pressure_angle)
            geom = g.get_geometry(bore = 0.125)

            scale = 500
            margin_factor = 0.2
            _style = {'stroke': 'red', 
                'stroke-width': 0.005, 
                'fill': 'transparent' }

            geom.write_svg(name, scale, style=_style)

            add_record(mycollection, newRecord)
            return name
        
        elif side == 1: # internal gear
            return name
        elif side == 2: # chainwheel gear
            return name
        elif side == 3: # planetary gear
            return name

        return name
