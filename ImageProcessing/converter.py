import sys
import os
from PIL import Image

def convert_images(images):
    renamed = []
    for imagename in images:
        if imagename.endswith('.jpg'):
            renamed.append(imagename.replace('.jpg', '.png'))
    return images



# get arguments
src_rep = sys.argv[1]
dest_rep = sys.argv[2]


if not os.path.exists(dest_rep):
    os.mkdir(dest_rep)

#loop through the image folder
for filename in os.listdir(src_rep):
    img = Image.open(f'{src_rep}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{dest_rep}{clean_name}.png', 'png')
    print('all done')






