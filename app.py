# Import Library
from flask import Flask, render_template, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask
app = Flask(__name__)

# Inisiasi objek flask_restful
api = Api(app)

# Inisiaasi objek dari flask corps
CORS(app)

# Inisiai variabel kosong bertipe dictionary
indetitas = {} #variable global, dictionary = json

#membuat class resource
class ContohResource(Resource):
    # Method get dan post

    def get(self):
       # response = {"msg":"Hallo dunia, ini app restful pertamaku"}
        return indetitas
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        indetitas["nama"] = nama
        indetitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response

# Set up resaource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__== "__main__":
    app.run(debug=True, port=50005)