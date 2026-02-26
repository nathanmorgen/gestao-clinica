from core.contracts.decorators import contrato
from core.intervalo_tempo import IntervaloTempo


class Consulta:
    def __init__(self, medico, paciente, sala, intervalo):
        # --------------------
        # Pré-condições
        # --------------------
        if medico is None:
            raise ValueError("medico não pode ser nulo")
        if paciente is None:
            raise ValueError("paciente não pode ser nulo")
        if sala is None:
            raise ValueError("sala não pode ser nula")

        if intervalo is None:
            raise TypeError("intervalo não pode ser None")
        if not isinstance(intervalo, IntervaloTempo):
            raise TypeError("intervalo deve ser IntervaloTempo")

        # --------------------
        # Estado
        # --------------------
        self.medico = medico
        self.paciente = paciente
        self.sala = sala
        self.intervalo = intervalo

        # --------------------
        # Invariante estrutural
        # --------------------
        if not self._invariante():
            raise ValueError("Invariante da Consulta violada")

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