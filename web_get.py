# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/maestria_ciberseguridad'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Principal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo_pagina = db.Column(db.String(25))
    serie = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))

    def __init_(self,titulo_pagina,serie,descripcion):
        self.titulo_pagina = titulo_pagina
        self.serie = serie
        self.descripcion = descripcion

#Esquema Principal
class PrincipalSchema(ma.Schema):
    class Meta:
        fields = ('descripcion','serie','titulo_pagina','id')

principal_schema = PrincipalSchema()

# Cuando sean muchas respuestas
principal_schema = PrincipalSchema(many=True)

#GET
@app.route('/', methods=['GET'])
def get_principal():
    all_principal = Principal.query.all()
    result = principal_schema.dump(all_principal)
    return jsonify(result)

# mensaje de bienvenida

@app.route('/',methods=['GET'])

def index():
    return jsonify({'Mensaje':'Bienvenido'})

if __name__=="__main__":
    app.run(debug=True)