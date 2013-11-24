#!/usr/bin/env python
import sys
import os
import re
import configparser
import argparse
import datetime

POSTS_PATH = "/home/jadavis/src/davis_clanin/site/_posts"
IMG_PATH = "/mnt/media/honora_pics/scaled/"
MONTH_ABBREV = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
file_template = """
---
categories: pic of the day
author: Jad
tags: 
date: %(slash_date)s 12:00:00
title: %(abbrev_month_date)s Pic of the Day 
draft: true
---
%(figure_stanzas)s
"""

figure_stanza = """

<figure>
<img src="%s" />
<figcaption></figcaption>
</figure>
"""

def main():
    POST_CREATOR_DIR = os.path.dirname(os.path.abspath(__file__))
    post_key = {}
    args = get_args()
    if args.config:
        config = get_config(POST_CREATOR_DIR, args.config)
    else:
        config = get_config(POST_CREATOR_DIR)
    posted_images = get_posted_images()
    existing_images = get_existing_images()
    #print (posted_images)
    #print (existing_images)
    for key in existing_images.keys():
        add_modify_post = False
        new_images = []
        match = re.search('(\d{4})(\d{2})(\d{2})', key) 
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        file_path = os.path.join(POSTS_PATH,match.group(0) + ".md")
        for image in existing_images[key]:
            key_image = "%s%s"%(key, image)
            if key_image not in posted_images:
                add_modify_post = True 
                new_images.append(image)
        if add_modify_post:
            print("New images %s"%new_images)
            print(file_path)
            if os.path.isfile(file_path):
                fp = open(file_path, 'a')
            else:
                fp = open(file_path, 'w')
                create_new_post(fp, year, month, day)

def add_images_to_existing_post(file_path, existing_images):
    return 0

def create_new_post(fp, year, month, day):
    print("Creating New Post")
    slash_date = "%s/%s/%s"%(year,month,day)
    abbrev_month_date = "%s. %s"%(MONTH_ABBREV[int(month)-1], day)
    figure_stanzas = "fig_stanz"
    print(file_template%{'slash_date':slash_date, 
        'abbrev_month_date':abbrev_month_date,
        'figure_stanzas':figure_stanzas})
    return 0
    fp.write(file_template%{'slash_date':slash_date, 
        'abbrev_month_date':abbrev_month_date,
        'file_stanzas':file_stanzas})



def get_posted_images():
    posted_images = {}
    for root, dirs, files in os.walk(POSTS_PATH):
        for file in files:
            fh = open(os.path.join(root, file), 'r')
            for line in fh:
                match = re.search('(\d{4})\/(\d{2})\/(\d{2})\/(img_\d{4}.*jpg)', 
                    line)
                if match:
                    key = "%s%s%s%s"%(match.group(1), match.group(2), 
                        match.group(3), match.group(4))
                    posted_images[key] = match.group(4)
    return posted_images

def get_existing_images():
    existing_images = {}
    for root, dirs, images in os.walk(IMG_PATH):
        if not dirs: # at a "node" with only images
            for image in images:
                if not re.search('small|large', image):
                    match = re.search('(\d{4})\/(\d{2})\/(\d{2})',
                            root)
                    key = "%s%s%s"%(match.group(1), 
                        match.group(2), match.group(3))
                    if key in existing_images:
                        existing_images[key].append(image)
                    else:
                        existing_images[key] = [image,]
    return existing_images

def get_config(root_dir, config_file=''):
    if not config_file:
        config_file = os.path.join(root_dir, os.pardir, 'conf', 'post_creator.ini')
    config = configparser.SafeConfigParser()
    config.read(config_file)
    return config


def get_args():
    parser = argparse.ArgumentParser(description='Autogenerate posts for davis-clanin.com.')
    parser.add_argument('-c', '--config', help='Specify config file')
    return parser.parse_args()


if __name__ == "__main__":
    main()