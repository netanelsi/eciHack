#!flask/bin/python
from flask import Flask, jsonify
from gopigo import *
import time

app = Flask(__name__)


@app.route('/todo/go_forward', methods=['GET'])
def go_forward(DistanceInCm):
    enable_encoders()
    ActualEncoderReading = enc_read(0)
    EncoderSteps = (DistanceInCm / (6.3 * 3.14)) * 18
    FinalEncoderStep = ActualEncoderReading + EncoderSteps

    fwd()

    while enc_read(0) < FinalEncoderStep
        time.wait(0.1)
        continue

    stop()

    return 'go foreward'



@app.route('/todo/go_backward', methods=['GET'])
def go_backward():
    return 'backward is not support'


@app.route('/todo/go_right', methods=['GET'])
def go_right():
    right()
    time.wait(0.1)
    stop()

    return 'go right'


@app.route('/todo/go_left', methods=['GET'])
def go_left():
    left()
    time.wait(0.1)
    stop()

    return 'go left'


@app.route('/todo/init', methods=['GET'])
def FirstSetp(NumOfCars, RequiredDistance):
    MyCarId = 0;
    DistanceToMove = (RequiredDistance * (NumOfCars - 1)) - (MyCarId * RequiredDistance)
    go_forward(DistanceToMove)
    return

if __name__ == '__main__':
    app.run(debug=True)

