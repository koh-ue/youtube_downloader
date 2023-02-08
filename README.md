# YOUTUBE_DOWNLOADER

This project is for downloading youtube videos from a single url or a playlist url.

## Usage

All required anaconda packages are listed in `conda_requirements.txt`. 
You can create the same anaconda environment by 

`conda create --name <ENVIRONMENT_NAME> --file conda_requirements.txt`.

### Minimum Usage 

`python src/script/base/youtube_download.py --url <VIDEO_URL>`

This command will download `<VIDEO_URL>` in `downloads` folder.

### Options

- `-h, --help`
	- show help message.
- `--video_dir <VID_DIR>`
	- set directory for saved videos.
- `--format`
	- set format for video like .mp4, .mp3, ....

