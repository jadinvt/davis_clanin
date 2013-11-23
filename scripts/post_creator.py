#!/usr/bin/env python
import sys
import os
import re
import configparser
import argparse
import datetime

POSTS_PATH = "/home/jadavis/src/davis_clanin/site/_posts"
IMG_PATH = "/mnt/media/honora_pics/scaled/"

file_template = """
---
categories: pic of the day
author: Jad
tags: 
date: %s 12:00:00
title: %s Pic of the Day 
draft: true
---
%s
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
    for key in existing_images.keys():
        for image in existing_images[key]:
            key_image = "%s-%s"%(key, image)
            if key_image not in posted_images:
                print existing_images[key]



def get_posted_images():
    posted_images = {}
    for root, dirs, files in os.walk(POSTS_PATH):
        for file in files:
            fh = open(os.path.join(root, file), 'r')
            for line in fh:
                match = re.search('(\d{4})\/(\d{2})\/(\d{2})\/(img_\d{4}.*jpg)', 
                    line)
                if match:
                    key = "%s-%s-%s-%s"%(match.group(1), match.group(2), 
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
                    key = "%s-%s-%s"%(match.group(1), 
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