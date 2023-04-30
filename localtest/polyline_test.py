

def makeHorizontalJagLine(x0, x1, y0, depth=3):
    lengthOfLine = x1-x0
    polylines = []
    if(lengthOfLine <= depth):
        print("too short!")
        polylines= [(x0, y0),(x1, y0)]
        return polylines

    y = True
    polylines.append((x0, y0))
    for x in range(1,9):    # divide into 9 segments (must be odd to end with same direction)
        if y:
            polylines.append(((x1-x0)*(x/9), y0))
            polylines.append(((x1-x0)*(x/9), y0-depth))
        else:
            polylines.append(((x1-x0)*(x/9), y0-depth))
            polylines.append(((x1-x0)*(x/9), y0))
        y = not y
    polylines.append((x1, y0))

    return polylines

def makeVerticalJagLine(y0, y1, x0, depth=3):
    lengthOfLine = y1-y0
    polylines = []
    if(lengthOfLine <= depth):
        print("too short!")
        polylines= [(x0, y0),(x0, y1)]
        return polylines

    x = True
    polylines.append((x0, y0))
    for y in range(1,9):    # divide into 9 segments (must be odd to end with same direction)
        if x:
            polylines.append((x0, (y1-y0)*(y/9)))
            polylines.append((x0-depth, (y1-y0)*(y/9)))
        else:
            polylines.append((x0-depth, (y1-y0)*(y/9)))
            polylines.append((x0, (y1-y0)*(y/9)))
        x = not x
    polylines.append((x0, y1))

    return polylines

length = 100
width = 60

#polylines=makeHorizontalJagLine(0, width, 0)
polylines=makeVerticalJagLine(0, length, 0)
print(polylines)