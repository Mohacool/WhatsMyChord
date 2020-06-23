from flask import Flask, render_template, request, jsonify

import io

import numpy as np

import random
from flask import Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/messages', methods = ['POST'])
def api_message():


    """
    my_buffer = request.get_data() # get buffer


    print "length of buffer is "+ str(len(my_buffer))
    """

    length = request.headers["Content-Length"]
    buffer = request.get_data(length)  

   
    my_array = np.frombuffer(buffer,dtype="float32") # convert buffer to numpy (error is here)


    # to csv
    
    a = np.asarray(my_array)
    np.savetxt("blah.csv", a, delimiter=",")

    #my_array = np.frombuffer(my_buffer,dtype="float32") # convert buffer to numpy (error is here)


    
    #print "length of my_array is "+ str(len(my_array))

    
    
    



    """
    length = request.headers["Content-Length"]
    Binaryfile = request.get_data(length)  

    #print "Binaryfile is type:"+ str(type(Binaryfile)) #bytestring 

    binary = io.BytesIO(Binaryfile) #bytestring -> IO.BYTE

    

    #print "Binary is type:"+ str(type(binary))

    
    data, samplerate = sf.read(io.BytesIO(Binaryfile),format='RAW',samplerate=44100,channels=2,subtype='FLOAT')


    import numpy
    a = numpy.asarray(data)
    numpy.savetxt("blah.csv", a, delimiter=",")

    
    print(data.shape)
    """


    
    
    


    """
    import numpy as np
    from scipy.io.wavfile import write

    data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
    scaled = np.int16(data/np.max(np.abs(data)) * 32767)
    write('test.wav', 44100, scaled)
    """

    return "Binary message written!"



@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response



if __name__ == "__main__":
    app.run()
