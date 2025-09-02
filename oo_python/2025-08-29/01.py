import pprint
import sys

import flask
import httpx
import requests

# o requests.get serve para fazer requisições HTTP
# o httpx.get é uma alternativa ao requests, com mais funcionalidades
# ambos retornam um objeto Response que tem o atributo .status_code
print('requests:', requests.get('https://api.github.com').status_code)
print('pprint:', httpx.get('https://api.github.com').status_code)

from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)