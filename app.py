import os
from flask import Flask
app = Flask(__name__)

HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 80)
HOST_NAME = os.getenv('HOST_NAME', 'none')

@app.route('/')
def hello_world():
    return 'Hello, Docker! This application is running on host: {0} \n'.format(HOST_NAME)

if __name__== '__main__':
    print('Server is running: {0}:{1} on host name {2} \n'.format(HOST, PORT, HOST_NAME))
    app.run(host=HOST, port=PORT)
