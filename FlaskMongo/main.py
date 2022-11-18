from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato

app = Flask(__name__)
cors = CORS(app)

##     Variables globales    ##
###############################

miControladorPartido = ControladorPartido()
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()

##      Probar Servicio      ##
###############################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running... OK"
    return jsonify(json)

##      EndPoint Partidos      ##
#################################

@app.route("/partidos", methods=["GET"])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=["POST"])
def crearPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["GET"])
def getpartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["PUT"])
def modificarPartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["DELETE"])
def eliminarPartidos(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)


if __name__ == "__main__":
    app.run(debug=False, port=9000)