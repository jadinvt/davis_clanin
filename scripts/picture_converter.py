#!/usr/bin/env python3
from PIL import Image
import sys
import os
from PIL.ExifTags import TAGS
import errno

large_scale = 3
medium_scale = 8
small_scale = 24


def main():
    for target in sys.argv[1:]:
        filename = os.path.basename(target)

        fullpath = os.path.abspath(target)
        (year, month, day) = fullpath.split("/")[4:7]

        path = "/mnt/media/honora_pics/scaled/%s/%s/%s/" % (year, month, day)
        print ("path: %s%s"%(path,target))

        mkdir_p(path)
        filename_body, fileextension = os.path.splitext(filename)
        filename_body = filename_body.lower()

        photo = Image.open(fullpath)

        (width, height) = photo.size
        large_photo = photo.resize((int(width/large_scale),int(height/large_scale)), 
                Image.ANTIALIAS)

        large_photo.save("%s/%s_large.jpg"%(path,filename_body), quality=95,optimize=True, dpi=(72,72))

        medium_photo = photo.resize((int(width/medium_scale),int(height/medium_scale)), 
                Image.ANTIALIAS)

        medium_photo.save("%s/%s_medium.jpg"%(path,filename_body), quality=95,optimize=True, dpi=(72,72))

        small_photo = photo.resize((int(width/small_scale),int(height/small_scale)), 
                Image.ANTIALIAS)

        small_photo.save("%s/%s_small.jpg"%(path,filename_body), quality=95,optimize=True, dpi=(72,72))

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

if __name__ == "__main__":
    main()
