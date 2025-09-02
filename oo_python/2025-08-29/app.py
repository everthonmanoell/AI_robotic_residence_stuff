from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return '<b>Bem-vindo ao Flask!</b>'
if __name__=='__main__':
    app.run(debug=True)