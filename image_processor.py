#!/usr/bin/env python3


from PIL import Image
import os


for dir, sub, files in os.walk('./images'):
    for file in files:
        if file[0:2] == 'ic':
            in_path = os.path.join('./images', file)
            #print(in_path)
            im = Image.open(in_path)
            out_path = os.path.join('./opt/icons',file)
            #print(out_path)
            im.resize((128, 128)).rotate(90).convert('RGB').save(out_path,'JPEG')
