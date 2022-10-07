from __future__ import unicode_literals
import youtube_dl
import tqdm
import os
import glob
import sys
import ffmpeg

class YOUTUBE_DOWNLOADER:
    def __init__(self):
        self.VIDEO_DIR = os.path.join(os.getcwd(), "downloads")
        self.OPTS = {
            "outtmpl": "{VIDEO_DIR}/%(title)s.mp4".format(VIDEO_DIR=self.VIDEO_DIR),
            'cachedir': False,
            'ignoreerrors': True
        }

    def download(self, url):
        print("Downloading {url} start..".format(url=url))
        with youtube_dl.YoutubeDL(self.OPTS) as y:
            info = y.extract_info(url, download=True)
            print("Downloading {url} finish!".format(url=url))
        return info

    def to_mp4(self, path):
        ext = os.path.splitext(path)
        filename = path.split('.')[0] + ".mp3"
        if "　" in filename:
            filename.replace("　", "_")
        if " " in filename:
            filename.replace(' ', '_')
        if ext[-1] != '.mp4':
            stream = ffmpeg.input(path)
            stream = ffmpeg.output(stream, filename)
            ffmpeg.run(stream)
            os.remove(path)

    def make_downloads_mp4(self):
        download_path = self.VIDEO_DIR
        files = os.listdir(download_path)
        print(files)
        files_file = [f for f in files if os.path.isfile(os.path.join(download_path, f))]
        for file in files_file:
            if file != '.DS_Store':
                path = download_path + "/" + file
                self.to_mp4(path)

    def download_playlist(self, url):
        info = self.download(url)
        self.make_downloads_mp4()


if __name__ == '__main__':
    link = input("URL:") #'https://www.youtube.com/playlist?list=PLrPOLFdAn_K__zPc0qtnVWv1EN-BKrx2L'
    ydl = YOUTUBE_DOWNLOADER()
    ydl.download_playlist(link)
    ydl.make_downloads_mp4()
