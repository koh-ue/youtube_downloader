from __future__ import unicode_literals

import os
import sys
import glob
from tqdm import tqdm
import ffmpeg
import youtube_dl

def download(url, video_dir):
    print("Downloading {url} start..".format(url=url))

    OPTS = {
                "outtmpl": "{VIDEO_DIR}/%(title)s".format(VIDEO_DIR=video_dir),
                'cachedir': False,
                'ignoreerrors': True
            }

    with youtube_dl.YoutubeDL(OPTS) as y:
        info = y.extract_info(url, download=True)
        print("Downloading {url} finish!".format(url=url))
    return info

def change_format(input_file, fmt):
    ext = os.path.splitext(input_file)
    output_file = ext[0] + fmt
    output_file.replace("　", "_").replace(' ', '_')

    if ext[-1] != fmt:
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file)
        ffmpeg.run(stream)
        os.remove(input_file)

def change_all_format(video_dir, fmt):
    files = os.listdir(video_dir)
    print(files)
    for file in tqdm(files):
        if file.split('.')[0] != '':
            file_name = video_dir + "/" + file
            change_format(file_name, fmt)