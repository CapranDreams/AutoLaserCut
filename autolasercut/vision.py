import tempfile, os
from autolasercut.utils import *
import cv2
import numpy as np
from PIL import Image

class Vision:
    def handle_uploaded_file(self, f, _name):
        with open("autolasercut/autolasercut/static/uploads/"+_name+".png", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return "/static/uploads/"+_name+".png"

    def rasterize_img(_name, _img, _thresh=125, _inv=False):
        name = _name
        img = cv2.imread("autolasercut/autolasercut/"+_img, cv2.IMREAD_GRAYSCALE)

        if name[-4:] != ".png":
            name = name + "_cv.png"
        db_path = "/static/uploads/" + name
        fullpath = "autolasercut/autolasercut/static/uploads/" + name
        name = fullpath

        if _inv:
            img = ~img
        raster_thresh = _thresh
        _,thresh = cv2.threshold(img,raster_thresh,255,cv2.THRESH_BINARY)
        img = cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB)
        # looks like image is actually in BGR space for some reason...
        img[np.where((img==[0,0,0]).all(axis=2))] = [255,0,0]
        #img[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]

        cv2.imwrite(name, img)

        #mycollection = get_collection('toolpaths', 'images')
        #newRecord = new_image_record(_name, db_path)
        #add_record(mycollection, newRecord)

        return db_path

    def dither_img(self, _name, _img, _type, _resolution):
        name = _name

        if name[-4:] != ".png":
            name = name + "_cv.png"
        db_path = "/static/uploads/" + name
        fullpath = "autolasercut/autolasercut/static/uploads/" + name
        name = fullpath

        img = Image.open("autolasercut/autolasercut/"+_img)
        img = img.convert('L')

        width, height = img.size
        new_width = _resolution
        new_height = int(height * new_width / width)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        nc = 2
        folder = "/static/uploads/"
        dim_path = folder+_name+'_dimg2.jpg'
        rim_path = folder+_name+'_rimg2.jpg'
        if _type == 0:
            dim = self.fs_dither(img, nc, new_width, new_height)
            img = np.array(dim) 
            _tp_type = "dither"
        else:
            rim = self.palette_reduce(img, nc, new_width, new_height)
            img = np.array(rim) 
            _tp_type = "recolor"
            
        img = ~img
        img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        img[np.where((img==[255,255,255]).all(axis=2))] = [255,0,0]
        img[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]
        cv2.imwrite(name, img)

        mycollection = get_collection('toolpaths', 'tp')
        newRecord = new_record(_name, _tp_type, db_path)
        add_record(mycollection, newRecord)

        return db_path

    def trace_img(self, _name, _img, _thresh1=50, _thresh2=100, _inv=False):
        name = _name
        img = cv2.imread("autolasercut/autolasercut/"+_img, cv2.IMREAD_GRAYSCALE)

        if name[-4:] != ".png":
            name = name + "_cv.png"
        db_path = "/static/uploads/" + name
        fullpath = "autolasercut/autolasercut/static/uploads/" + name
        name = fullpath

        if _inv:
            img = ~img

        img_blur = cv2.GaussianBlur(img,(3,3), sigmaX=0, sigmaY=0) 

        # Sobel Edge Detection
        #sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        #sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        #sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=_thresh1, threshold2=_thresh2) 

        img = cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
        
        img[np.where((img==[255,255,255]).all(axis=2))] = [0,0,255]
        #img[np.where((img==[255,255,255]).all(axis=2))] = [0,0,0]
        img[np.where((img==[0,0,0]).all(axis=2))] = [255,255,255]
        
        cv2.imwrite(name, img)
        
        mycollection = get_collection('toolpaths', 'tp')
        newRecord = new_record(_name, "trace", db_path)
        add_record(mycollection, newRecord)

        return db_path


    def get_new_val(self, old_val, nc):
        """
        Get the "closest" colour to old_val in the range [0,1] per channel divided
        into nc values.

        """

        return np.round(old_val * (nc - 1)) / (nc - 1)

    # For RGB images, the following might give better colour-matching.
    #p = np.linspace(0, 1, nc)
    #p = np.array(list(product(p,p,p)))
    #def get_new_val(old_val):
    #    idx = np.argmin(np.sum((old_val[None,:] - p)**2, axis=1))
    #    return p[idx]

    def fs_dither(self, img, nc, new_width, new_height):
        """
        Floyd-Steinberg dither the image img into a palette with nc colours per
        channel.

        """

        arr = np.array(img, dtype=float) / 255

        for ir in range(new_height):
            for ic in range(new_width):
                # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
                old_val = arr[ir, ic].copy()
                new_val = self.get_new_val(old_val, nc)
                arr[ir, ic] = new_val
                err = old_val - new_val
                # In this simple example, we will just ignore the border pixels.
                if ic < new_width - 1:
                    arr[ir, ic+1] += err * 7/16
                if ir < new_height - 1:
                    if ic > 0:
                        arr[ir+1, ic-1] += err * 3/16
                    arr[ir+1, ic] += err * 5/16
                    if ic < new_width - 1:
                        arr[ir+1, ic+1] += err / 16

        carr = np.array(arr/np.max(arr, axis=(0,1)) * 255, dtype=np.uint8)
        return Image.fromarray(carr)


    def palette_reduce(self, img, nc, new_width, new_height):
        """Simple palette reduction without dithering."""
        arr = np.array(img, dtype=float) / 255
        arr = self.get_new_val(arr, nc)

        carr = np.array(arr/np.max(arr) * 255, dtype=np.uint8)
        return Image.fromarray(carr)
