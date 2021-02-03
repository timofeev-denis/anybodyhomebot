import os
import sys
sys.path.append('/home/t/tdv01/code4fun.ru/public_html/e2a87cee-664c-11eb-ae93-0242ac130002/myenv/lib/python3.6/site-packages/')
from flask import Flask
app = Flask(__name__)
application = app

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

if __name__ == '__main__':
    app.run()
