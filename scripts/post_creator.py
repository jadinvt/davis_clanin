#!/usr/bin/env python
import sys
import os
import configparser
import argparse
import datetime

POSTS_PATH = "/home/jadavis/src/davis_clanin/site/_posts"
IMG_PATH = "/mnt/media/honora_pics/scaled/"

def main():
    POST_CREATOR_DIR = os.path.dirname(os.path.abspath(__file__))
    args = get_args()
    if args.config:
        config = get_config(POST_CREATOR_DIR, args.config)
    else:
        config = get_config(POST_CREATOR_DIR)
    posted_images = get_posted_images()
    existing_images = get_existing_images()



def get_posted_images():
    return []

def get_existing_images():
    return []

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