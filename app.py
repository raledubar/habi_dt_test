from flask import Flask, request, jsonify, make_response
import handlers

app = Flask(__name__)


@app.route('/inmuebles', methods=['GET'])
def get_inmuebles_api():
    # inmuebles = handlers.get_inmuebles()
    inmuebles = handlers.filter_inmuebles()
    return make_response(jsonify({"inmuebles": inmuebles}))


if __name__ == '__main__':
    app.run(debug=True)
