import os

os.system("pip install py3exiv2")
os.system("pip3 install py3exiv2")

import py3exiv2

# Get the current working directory
directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the image file in the same directory
# video_path = os.path.join(directory, 'video.mp4')
video_path = os.path.join(directory, video_file)

def remove_metadata(video_file):
    metadata = py3exiv2.ImageMetadata(video_file)
    metadata.read()

    for key in metadata.exif_keys:
        metadata.delete(key)
    for key in metadata.iptc_keys:
        metadata.delete(key)
    for key in metadata.xmp_keys:
        metadata.delete(key)

    metadata.write()

def clean_video_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):  
                video_file = os.path.join(root, file)
                remove_metadata(video_file)
                print(f"Метаданные удалены из {video_file}")
# Добавьте другие расширения, если необходимо

# Пример использования
clean_video_directory('video_path')

# softy_plug