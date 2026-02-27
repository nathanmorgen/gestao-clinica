from core.contracts.decorators import contrato
from core.intervalo_tempo import IntervaloTempo


class Consulta:
    """
    Consulta é um Value Object rico.
    Neste estágio do domínio, não possui identidade própria.
    """

    @contrato(
        pre=lambda self, medico, paciente, sala, intervalo: (
            medico is not None
            and paciente is not None
            and sala is not None
            and isinstance(intervalo, IntervaloTempo)
        ),
        invariante=lambda self: self._invariante()
    )
    def __init__(self, medico, paciente, sala, intervalo):
        self.medico = medico
        self.paciente = paciente
        self.sala = sala
        self.intervalo = intervalo

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
    # Ponto semântico
    # --------------------
    @contrato(
        pre=lambda self: True,
        pos=lambda self, resultado: resultado is None,
        invariante=lambda self: self._invariante()
    )
    def validar(self):
        """
        Ponto explícito de verificação contratual.
        """
        return None