import os

from PIL import Image
from PIL import GifImagePlugin


def askDir():
    os.chdir(input('where is the working directory?...'))
    directory = os.path.abspath(os.getcwd())
    return directory

def gifCollecter(directory):
    gif_list = [file for file in os.listdir(directory) if file.endswith("gif")]
    return gif_list


def gifCutter(directory,gif_list):
    for gif in gif_list:
        image_obj = Image.open(f"{directory}/{gif}")
        print(image_obj.is_animated)
        print(image_obj.n_frames)
        for frame in range(0,image_obj.n_frames):
            try:
                image_obj.seek(frame)
            except EOFError:
                print("EOFERROR DECTECTED")
                pass
            print(frame)
            image_obj.save(f"{directory}/{gif[:-4]}_{frame}.png", quality = 100)
            Image.open(f"{directory}/{gif[:-4]}_{frame}.png").convert("RGB").save(f"{directory}/{gif[:-4]}_{frame}.jpg", quality = 100)


while True:
    directory = askDir()
    gif_list = gifCollecter(directory)
    print(gif_list)
    gifCutter(directory,gif_list)
