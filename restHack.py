#!flask/bin/python
from flask import Flask, jsonify
from gopigo import *
import time

app = Flask(__name__)
app.config['SERVER_NAME'] = '192.168.43.195:5000'


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/go_forward', methods=['GET'])
def go_foreward(DistanceInCm = 5):
    enable_encoders()
    ActualEncoderReading = enc_read(0)
    EncoderSteps = (DistanceInCm / (6.3 * 3.14)) * 18
    FinalEncoderStep = ActualEncoderReading + EncoderSteps

    fwd()

    while enc_read(0) < FinalEncoderStep:
        time.sleep(0.1)
        continue

    stop()

    return 'go foreward'



@app.route('/todo/go_backward', methods=['GET'])
def go_backward():
    return 'backward is not support'


@app.route('/todo/go_right', methods=['GET'])
def go_right():
    print('aa')
    right()
    print('bb')
    # time.wait(0.1)
    time.sleep(1)
    print('cc')
    stop()

    return 'go right'


@app.route('/todo/go_left', methods=['GET'])
def go_left():
    left()
    time.sleep(0.1)
    stop()

    return 'go left'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = int('5000'),debug=True)
