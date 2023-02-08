from __future__ import unicode_literals

import os
import sys
import glob
from tqdm import tqdm
import ffmpeg
import argparse
import youtube_dl

sys.path.append(".")

from src.library.core.downloader import download, change_format, change_all_format

parser = argparse.ArgumentParser()

parser.add_argument('--url', type=str, required=True)
parser.add_argument('--video_dir', type=str, default="downloads")
parser.add_argument('--format', type=str, default=".mp4")

args = parser.parse_args()

def youtube_download(url, video_dir, fmt):
    download(url, video_dir)
    change_all_format(video_dir, fmt)


if __name__ == '__main__':
    youtube_download(args.url, args.video_dir, args.format)
