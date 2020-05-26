# -*- coding: utf-8 -*-
"""
Created on Sat May 23 20:02:55 2020

@author: Mohamed
"""

# Improting Image class from PIL module 
from PIL import Image 
import os
  
# Opens a image in RGB mode 

im_name = "F#major-0.jpg"
im_name = "F#aug9-3.jpg"

# (x,y,x+w,y+h)


for image_path in os.listdir(os.getcwd()):
    
    if not os.path.exists('cropped/'+image_path):
        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            print(image_path)
            im = Image.open(image_path) 
        
               
            width, height = im.size 
        
            im1 = im.crop((0, 90, width-40, height)) 
        
            rgb_im = im1.convert('RGB')
            rgb_im.save('cropped/'+image_path)



  
# Shows the image in image viewer 
#im1.show() 
                