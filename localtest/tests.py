import pytest


# SVGwrite tests
import svgwrite
import os.path
def test_svg_save():
    box_width = 200
    box_height = 100
    box_position = (0,0)
    box_radius = 0
    _stroke = 3
    filename = 'autolasercut/localtest/testRect.svg'
    dwg = svgwrite.Drawing(filename, profile='tiny')
    dwg.add(svgwrite.shapes.Rect(insert=box_position, size=(box_width, box_height), rx=box_radius, ry=box_radius, fill='white', stroke='red', stroke_width=_stroke))
    dwg.save()
    assert os.path.isfile(filename)

# MongoDB tests
import autolasercut.localtest.mongoDB as db
def test_db_connect_to_collection():
    myDB = db.get_database()
    assert 'tp' in myDB.list_collection_names()
def test_db_connect_to_bad_collection():
    myDB = db.get_database()
    assert 'fake_collection' not in myDB.list_collection_names()
def test_db_add_record():
    myDB = db.get_database()
    myCollection = myDB['test']
    startSize = myCollection.count_documents({})
    db.create_random_record(myCollection)
    assert startSize + 1 == myCollection.count_documents({})
