from flask import Flask, render_template, request, jsonify
from PlotSignal import plotSignal
from Identify import Identify

import io

import numpy as np

import random
from flask import Response

app = Flask(__name__)

sample_rate = 0

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/samplerate', methods = ['POST'])

def get_rate():

    """
    my_buffer = request.get_data() # get buffer


    print "length of buffer is "+ str(len(my_buffer))
    """
    print ("sample rate:")
    length = request.headers["Content-Length"]
    buffer = request.get_data(length)  

    global sample_rate
    sample_rate = buffer.decode("utf-8")
    
    return "Sample rate received!"


@app.route('/messages', methods = ['POST'])
def api_message():

    """
    my_buffer = request.get_data() # get buffer


    print "length of buffer is "+ str(len(my_buffer))
    """

    length = request.headers["Content-Length"]
    buffer = request.get_data(length)  

    #print (buffer) 

   
    my_array = np.frombuffer(buffer,dtype="float32") # convert buffer to numpy (error is here)

    global sample_rate
    print (sample_rate)

    # to csv
    a = np.asarray(my_array)
    np.savetxt("blah.csv", a, delimiter=",")

    #my_array = np.frombuffer(my_buffer,dtype="float32") # convert buffer to numpy (error is here)
    
    #print "length of my_array is "+ str(len(my_array))

    return "Binary message written!"


################################################################################
# CODE WITH SINGLE AJAX REQUEST
@app.route('/messages2', methods = ['POST'])
def api_message2():

    signal = request.form.getlist('audio[]')
    sampleRate = float(request.form['sampleRate'])
    if signal:
        signalArray = np.array(signal).astype(float)
        print("Success!")
        print(signalArray.shape)

        plotSignal(signalArray, sampleRate)
        notes = list(Identify(signalArray, sampleRate, drawPlots=True))

        return jsonify({'notes' : notes})

    return jsonify({'error' : 'no data'})
################################################################################

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response



if __name__ == "__main__":
    app.run()
