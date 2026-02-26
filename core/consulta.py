from core.contracts.decorators import contrato
from core.intervalo_tempo import IntervaloTempo


class Consulta:
    def __init__(self, medico, paciente, sala, intervalo):
        self.medico = medico
        self.paciente = paciente
        self.sala = sala
        self.intervalo = intervalo

        if not self._invariante():
            raise ValueError("Consulta inválida: atributos obrigatórios ausentes ou inválidos")

    # --------------------
    # Invariante estrutural
    # --------------------
    def _invariante(self):
        return (
            self.medico is not None
            and self.paciente is not None
            and self.sala is not None
            and isinstance(self.intervalo, IntervaloTempo)
        )

    # --------------------
    # Comportamento mínimo
    # --------------------
    @contrato(
        pre=lambda self: True,
        pos=lambda self, resultado: resultado is None,
        invariante=lambda self: self._invariante()
    )
    def validar(self):
        """
        Ponto semântico para verificação explícita de contrato.
        Útil para testes, snapshots e auditoria.
        """
        return None