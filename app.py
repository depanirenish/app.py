from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = os.environ["NAME"]
    return '<h1>Hello, World 1. '+ name  +'</h1>'

if __name__ == '__main__':
    # Specify the custom port number here
    app.run(debug=True, host='0.0.0.0', port=8080)
