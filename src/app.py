from flask import Flask
from flask import request
from generate_conditional import conditional
app = Flask(__name__)

@app.route('/')
def hello_world():
    input = request.args.get('input')
    top_k = request.args.get('top_k', 100, int)
    return input + ' : ' + conditional(raw_text_input=input, top_k=int(top_k))

@app.route('/ping')
def hello_test():
    return 'pong'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')