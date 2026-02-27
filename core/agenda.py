from core.contracts.decorators import contrato
from core.contracts.errors import InvarianteVioladaError


class Agenda:
    def __init__(self):
        self._consultas = []

    def _invariante_sem_conflitos(self):
        for i, a in enumerate(self._consultas):
            for b in self._consultas[i + 1:]:
                if a.intervalo.sobrepoe(b.intervalo):
                    if a.medico == b.medico or a.sala == b.sala:
                        return False
        return True

    @contrato(
        pre=lambda self, consulta: (consulta is not None and hasattr(consulta, "intervalo") and hasattr(consulta, "medico") and hasattr(consulta, "sala")),
        pos=lambda self, _: self._invariante_sem_conflitos(),
        invariante=lambda self: self._invariante_sem_conflitos()
    )
    def inserir(self, consulta):
        #proteger identidade (Aggregate Root rule)
        for existente in self._consultas:
            if existente.id == consulta.id:
                raise InvarianteVioladaError(
                    "Já existe consulta com o mesmo id na agenda."
                )

        #proteger conflitos de negócio
        for existente in self._consultas:
            if existente.intervalo.sobrepoe(consulta.intervalo):
                if existente.medico == consulta.medico:
                    raise InvarianteVioladaError("Conflito de médico")
                if existente.sala == consulta.sala:
                    raise InvarianteVioladaError("Conflito de sala")

        self._consultas.append(consulta)
    def consultas(self):
        return list(self._consultas)