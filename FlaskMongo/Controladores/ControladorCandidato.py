from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        self.candidatoRepositorio = RepositorioCandidato()
        self.partidoRepositorio = RepositorioPartido()

    def index(self):
        return self.candidatoRepositorio.finAll()
    
    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.candidatoRepositorio.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.candidatoRepositorio.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        elCandidato = Candidato(self.candidatoRepositorio.findById(id))
        elCandidato.cedula = infoCandidato["cedula"]
        elCandidato.no_resolucion = infoCandidato["no_resolucion"]
        elCandidato.nombre = infoCandidato["nombre"]
        elCandidato.apellido = infoCandidato["apellido"]
        return self.candidatoRepositorio.save(elCandidato)

    def delete(self, id):
        return self.candidatoRepositorio.delete(id)

    def asignarCandidato(self, id, id_partido):
        candidatoActual = Candidato(self.candidatoRepositorio.findById(id))
        partidoActual = Partido(self.partidoRepositorio.findById(id))
        candidatoActual.partido = partidoActual
        return self.candidatoRepositorio.save(candidatoActual)