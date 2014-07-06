#!/usr/bin/env python3
import os
import re
import sys


# fullpath = os.path.abspath(target)
#(year, month, day) = fullpath.split("/")[4:7]

#path = "/mnt/media/honora_pics/scaled/%s/%s/%s/" % (year, month, day)


def main(single_dir=None):
    dropbox_dir = '/home/jadavis/Dropbox/Camera Uploads'
    target_dir = '/home/jadavis/Desktop/latest_uploads'
    #dropbox_dir = '/home/jadavis/Desktop/Camera_alisa'
    #target_dir = '/mnt/media/Pictures/2014/06/09'
    if single_dir:
        dropbox_dir = target_dir = single_dir
    for file in os.listdir(dropbox_dir):
        match = re.search(
                '(\d{4})-(\d{2})-(\d{2}) (\d{2})\.(\d{2}).(\d{2}).(\w+)', file)
        if match:            
            newfilename = "img_%s%s%s%s%s%s.%s" % (
                    match.group(1, 2, 3, 4, 5, 6, 7))
            old_file = "%s/%s" % (dropbox_dir, file)
            new_file = "%s/%s" % (target_dir, newfilename)
            print("%s %s" % (old_file, new_file))
            result = os.rename(old_file, new_file)

if __name__ == "__main__":
    single_dir = None
    if len(sys.argv) == 2:
        single_dir = sys.argv[1]
    main(single_dir)
