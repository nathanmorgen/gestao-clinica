class Agenda:
    def __init__(self):
        self._consultas = []

    def inserir(self, consulta):
        for existente in self._consultas:
            if existente.intervalo.sobrepoe(consulta.intervalo):
                if existente.medico == consulta.medico:
                    raise ValueError("Conflito de médico")
                if existente.sala == consulta.sala:
                    raise ValueError("Conflito de sala")
        self._consultas.append(consulta)

    def consultas(self):
        return list(self._consultas)
