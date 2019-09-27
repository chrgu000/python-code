from flask import Flask, abort, request 
import json
from send_sms import SMS


app = Flask(__name__)

@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    print("type: ", type(request.json))
    print(request.json)
    
    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)