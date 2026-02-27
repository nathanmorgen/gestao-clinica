from core.contracts.decorators import contrato
from core.intervalo_tempo import IntervaloTempo
from core.entity_id import EntityId


class Consulta:
    """
    Consulta é uma Entidade.
    Possui identidade própria e igualdade baseada exclusivamente em EntityId.
    """

    @contrato(
        pre=lambda self, id, medico, paciente, sala, intervalo: (
            isinstance(id, EntityId)
            and medico is not None
            and paciente is not None
            and sala is not None
            and isinstance(intervalo, IntervaloTempo)
        ),
        invariante=lambda self: self._invariante()
    )
    def __init__(self, id: EntityId, medico, paciente, sala, intervalo):
        self._id = id
        self.medico = medico
        self.paciente = paciente
        self.sala = sala
        self.intervalo = intervalo

    # --------------------
    # Propriedade de identidade (somente leitura)
    # --------------------
    @property
    def id(self) -> EntityId:
        return self._id

    # --------------------
    # Invariante estrutural
    # --------------------
    def _invariante(self):
        return (
            isinstance(self._id, EntityId)
            and self.medico is not None
            and self.paciente is not None
            and self.sala is not None
            and isinstance(self.intervalo, IntervaloTempo)
        )

    # --------------------
    # Igualdade por identidade
    # --------------------
    def __eq__(self, other):
        if not isinstance(other, Consulta):
            return False
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

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