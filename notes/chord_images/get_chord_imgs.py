# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:19:18 2020

@author: Mohamed
"""

import requests

import os.path
from os import path

chord_folder = '/chord_images/'

import json

new_data = {}

with open('../guitar.json') as f: 
    data = json.load(f)
    
new_data = {}

'''
new_data['key'] = 'value'
json_data = json.dumps(new_data)
'''

for chord in data["chords"]:
    
    chord_num = 0 
    for thing in data["chords"][chord]:
        name = thing["key"]+thing["suffix"]
        file_name = name
        
        number = 0
        for p in thing["positions"]:
            chord_num += 1
            capo = p["baseFret"]
            
            if capo>1:
                chord = p['frets']
                
                # Adjust for no capo
                

                chord = [x+capo-1 if x!=-1 else -1  for x in chord]
                
                

            else:
                chord = p['frets']
                # just return the chord as is
            
            finger = p['fingers']
            
            chord = ['x' if (x==-1) else x for x in chord]
            finger = ['-' if (x==0) else x for x in finger]
            
            if any (x>=10 for x in chord):
                    chord = [str(x)+'-' for x in chord]
                    chord[-1] = chord[-1][:-1]
            
            chord_str = ''.join(str(e) for e in chord)
            finger_str = ''.join(str(e) for e in finger)
            
            chord_name = file_name + '-'+str(number)
            chord_name = chord_name.replace('/','ov')
            
            name = name.replace('major','')
            name = name.replace('minor','m')
            name = name.replace('#','%23')
                                
                    
                                
            if not path.exists(chord_name+'.jpg'):
           
                image_url = "https://chordgenerator.net/.png?p="+chord_str+"&f="+finger_str+"&s=8"
                
                if chord_name in ["F#aug7-3"]:
                    print(chord)
                    print(chord_str)
                    print(finger_str)
                    print(image_url)
                    
                
                img_data = requests.get(image_url).content
                with open(chord_name+'.jpg', 'wb') as handler:
                    handler.write(img_data)
                
                if name in new_data.keys():
                    new_data[name] += [[chord_name,chord_str,finger_str]]
                else:
                    new_data[name] = [[chord_name,chord_str,finger_str]]
                
                number +=1
                print(chord_num)
            
    





    