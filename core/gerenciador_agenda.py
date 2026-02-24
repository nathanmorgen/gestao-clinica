from core.agenda import Agenda
from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo

class GerenciadorAgenda:
    def __init__(self):
        self.agenda = Agenda()

    def agendar(self, medico, paciente, sala, inicio, fim):
        try:
            intervalo = IntervaloTempo(inicio, fim)
            consulta = Consulta(medico, paciente, sala, intervalo)
            self.agenda.inserir(consulta)
            return True
        except Exception as e:
            return False, str(e)
