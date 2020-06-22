from flask import Flask, render_template, request, jsonify

import io

import soundfile as sf
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt
from scipy.io.wavfile import write

import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import sys

import wave
import struct

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/messages', methods = ['POST'])
def api_message():
    # Open file and write binary (blob) data
    f = open('./file.wav', 'wb')
    f.write(request.get_data())
    f.close()

    length = request.headers["Content-Length"]
    Binaryfile = request.get_data(length)  

    print "Binaryfile is type:"+ str(type(Binaryfile))

    binary = io.BytesIO(Binaryfile)

    print "Binary is type:"+ str(type(binary))

    
    data, samplerate = sf.read(io.BytesIO(Binaryfile),format='RAW',samplerate=44100,channels=2,subtype='FLOAT')

    
    print(data.shape)


    """
    import numpy
    a = numpy.asarray(data)
    numpy.savetxt("blah.csv", a, delimiter=",")
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
    app.run(debug=True)
