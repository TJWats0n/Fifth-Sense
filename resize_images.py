import os
from PIL import Image

'''
Small script for automatically resizing all pictures contained in the basic dataset (without distinguishing train or 
test). Reduces the size of the dataset from ~3GB to 23.6 MB.
'''

base_path = os.path.join(os.getcwd(),'dataset')
width = 300 #in pixels
ratio = 1.5 #with to height ratio
height = round(width/ratio)

def resize_pictures(base_path):
    banknotes = list_dirs(base_path)
    print(banknotes)

    for banknote in banknotes:
        categories = list_dirs(banknote)
        print(categories)

        for category in categories:
            pictures = [os.path.join(category, picture) for picture in os.listdir(category) if picture[-3:] == 'JPG']

            for picture in pictures:
                img = Image.open(picture)
                os.remove(picture)#replacing
                img = img.resize(size=(width,height))
                img.save(picture)

#list only sub_dirs in input_dir
def list_dirs(input_dir):
    contained_dirs = [os.path.join(input_dir, sub_dir) for sub_dir in os.listdir(input_dir) if
                 os.path.isdir(os.path.join(input_dir, sub_dir))]
    return contained_dirs


if __name__ == '__main__':
    resize_pictures(base_path)