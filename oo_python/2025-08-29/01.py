import pprint
import sys

import flask
import httpx
import requests

print('requests:', requests.get('https://api.github.com').status_code)
print('pprint:', httpx.get('https://api.github.com').status_code)

from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)