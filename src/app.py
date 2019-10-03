from flask import Flask
from flask import request
from generate_conditional import conditional
app = Flask(__name__)

@app.route('/')
def generate():
    raw_text_input = request.args.get('input')
    model_name = request.args.get('model_name', '124M', str)
    seed = request.args.get('seed', None, int)
    nsamples = request.args.get('nsamples', 1, int)
    batch_size = request.args.get('batch_size', 1, int)
    length = request.args.get('length', None, int)
    temperature = request.args.get('temperature', 1, int)
    top_k = request.args.get('top_k', 100, int)
    top_p = request.args.get('top_p', 1, int)

    return conditional(raw_text_input, model_name, seed, nsamples, batch_size, length, temperature, top_k, top_p)

@app.route('/ping')
def test():
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