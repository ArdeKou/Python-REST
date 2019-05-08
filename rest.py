from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_sqlalchemy impirt SQLAlchemy
from sql import connect, query_fetchone, query_fetchall

app = Flask(__name__)
api = Api(app)

people = {}

people_fields = {
    'firstname': fields.String,
    'lastname': fields.String
}

class PeopleListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('firstname', type = str, required = True,
                                                location = 'json')
        self.reqparse.add_argument('lastname', type = str, required = True,
                                                location = 'json')
        super(PeopleListAPI, self).__init__()

        def get(self):
            return {'people': }

api.add_resource(PeopleListAPI, '/people', )

if __name__ == '__main__':
    app.run(debug=True)
