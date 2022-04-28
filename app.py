from flask import Flask, request, jsonify, make_response
import handlers
from models import Inmueble


app = Flask(__name__)


@app.route('/inmuebles', methods=['GET'])
def get_inmuebles_api():
    args = request.args
    data = handlers.filter_inmuebles()
    inmuebles = []
    for row in data:
        resource = Inmueble(*row)
        entity = dict(resource)
        inmuebles.append(entity)
    if args:
        handlers.save_filters(args)
        resources = []
        for resource in inmuebles:
            if handlers.check_filters(
                resource=resource,
                filters=args
            ):
                resources.append(resource)
        return make_response(jsonify({"inmuebles": resources}))
    return make_response(jsonify({"inmuebles": inmuebles}))


if __name__ == '__main__':
    app.run(debug=True)
