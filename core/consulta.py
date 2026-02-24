from core.intervalo_tempo import IntervaloTempo

class Consulta:
    def __init__(self, medico, paciente, sala, intervalo):
        if medico is None or paciente is None or sala is None:
            raise ValueError("Consulta inválida: objetos não podem ser nulos")

        if not isinstance(intervalo, IntervaloTempo):
            raise TypeError("intervalo deve ser IntervaloTempo")

        self.medico = medico
        self.paciente = paciente
        self.sala = sala
        self.intervalo = intervalo
