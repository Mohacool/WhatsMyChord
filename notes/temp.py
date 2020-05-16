# -*- coding: utf-8 -*-
import json


with open('guitar.json') as f:
    data = json.load(f)


new_data = {}

'''
new_data['key'] = 'value'
json_data = json.dumps(new_data)
'''

for chord in data["chords"]:
    if chord == "Dmajor":
        print("Dmajor")
    i = 0
    for thing in data["chords"][chord]:
        name = thing["key"]+thing["suffix"]
        
        #print (thing["positions"])
        pos = 0
        for p in thing["positions"]:
            capo = p["baseFret"]
            
            if capo>1:
                chord = p['frets']
                
                # Adjust for no capo
                

                chord = [x+capo-1 if x!=-1 else -1  for x in chord]

            else:
                chord = p['frets']
                # just return the chord as is
            
            
            if name in new_data.keys():
                new_data[name] += [chord]
            else:
                new_data[name] = [chord]
            pos +=1
            #print(pos)
            #print(chord)
        i+=1
        #print (data["chords"][chord])
        #print(i)
        

# Manual additions
        
new_data["D/E"] = [[0,0,0,2,3,2]]
new_data["D/G"] = [[3,0,0,2,3,2]]


with open('data.json', 'w') as f:
    json.dump(new_data, f)