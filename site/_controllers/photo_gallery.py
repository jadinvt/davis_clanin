# A stupid little photo gallery for Blogofile.

# Read all the photos in the /photos directory and create a page for each along
# with Disqus comments.

import os
import ipdb
from blogofile.cache import bf

config = {"name": "Photo Gallery",
          "description": "A very simplistic photo gallery, used as an example",
          "priority": 40.0}

photos_dir = os.path.join(".", "img")
photo_gallery_dir = "photo_gallery"

class Photo():

    def __init__(self, name, year, month, day):
        self.name = name

    def get_name(self):
        return self.name

    def _get_photo_date(self):
        return 0


def run():
    photos = read_photos()
    import ipdb;ipdb.set_trace()
    write_pages(photos)
    write_photo_index(photos)


def read_photos():
    photos = []

    for root, dirnames, filenames in os.walk('img'):
        if dirnames:
            continue
        (local, year, month, day) = root.split('/')
        for file in filenames:
            if file.lower().endswith("large.jpg"):
                photos.append(Photo(file, year, month, day))

    return photos


def write_pages(photos):
    for photo in photos:
        bf.template.materialize_template("photo.mako", os.path.join(photo_gallery_dir, photo.get_name() + ".html"), {"photo": photo})


def write_photo_index(photos):
    bf.template.materialize_template("photo_index.mako",
                                     os.path.join(photo_gallery_dir, "index.html"), {"photos": photos})
