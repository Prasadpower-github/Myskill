import json
from flask import Flask , jsonify,request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

@app.route('/')
def index():
    return json.dumps({'name' : 'DP',
                   'email': 'DXC'})

@app.route('/income')
def helloworld():
    return jsonify(incomes)



if __name__ == '__main__':
    
    app.run(debug=true)
   