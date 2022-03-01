from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class Version(Resource):
    def get(self):
        data = 0.01
        return {"current version": data}, 200

api.add_resource(Version, '/version')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)