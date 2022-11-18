import json

import certifi
from pymongo import MongoClient

ca = certifi.where()

####################################
#Cargar el archivo de configuracion#
####################################
def loadConfigFile():
    with open('C:\ProyectoCiclo4A_ACR\FlaskMongo\database\config.json') as f:
        data = json.load(f)
    return data

####################################
#        Funcion de conexion       #
####################################
def dbConnection ():
    dataConfig = loadConfigFile()
    try:
        #Conexion atlas#
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        #conexion local#
        #client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["Ciclo4_Resultados"]
    except ConnectionError:
        print("Error de conexion con la db")
    return db 