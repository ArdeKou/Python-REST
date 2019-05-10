from flask import Flask, abort, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostaddress/db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class python_dev(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))

class python_devSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstname", "lastname")
        sqla_session = db.session

python_dev_schema = python_devSchema()
python_devs_schema = python_devSchema(many=True)

@app.route('/people', methods=['GET'])
def get_people():
    all = python_dev.query.all()
    result = python_devs_schema.dump(all)
    return jsonify(result.data)

@app.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    print(python_dev.query.get(person_id))
    return python_dev_schema.jsonify(python_dev.query.get(person_id))

@app.route('/echo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def echo():
    if request.method == 'GET':
        return 'ECHO: GET\n'
    elif request.method == 'POST':
        return 'ECHO: POST\n'
    elif request.method == 'PUT':
        return 'ECHO: PUT\n'
    elif request.method == 'DELETE':
        return 'ECHO: DELETE\n'

@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return 'Text Message: ' + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return 'Binary message written!'

    else:
        return "415 Unsupported Media Type"

@app.route('/people', methods=['POST'])
def add_person():
    if not request.json or not 'firstname' in request.json:
        abort(400)
    elif not 'lastname' in request.json:
        abort(400)
    #person = {
    #        'firstname': request.json['firstname'],
    #        'lastname': request.json['lastname']
    #}
    #print(person)
    #jsonify(person)
    #new_person = python_dev_schema.load(person).data
    new_person = python_dev(firstname=(request.json['firstname']), lastname=(request.json['lastname']))
    db.session.add(new_person)
    db.session.commit()
    return 'Added to database'

@app.route('/people/<int:person_id>', methods=['DELETE'])
def del_person(person_id):
    per = python_dev.query.get(person_id)
    db.session.delete(per)
    db.session.commit()
    return 'deleted'

@app.route('/people/<int:person_id>', methods=['PUT'])
def edit_person(person_id):
    if not request.json:
        abort(400)
    per = python_dev.query.get(person_id)
    print(per)
    per.firstname = request.json['firstname']
    per.lastname = request.json['lastname']
    db.session.commit()
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)
