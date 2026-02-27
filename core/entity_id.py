# core/entity_id.py

from core.contracts.decorators import contrato


class EntityId:
    """
    Value Object que representa identidade semântica de entidades.

    - Imutável (após construção)
    - Comparável por valor
    - Hashable
    - Observável por contrato
    """

    __slots__ = ("_value", "_locked", "__dict__")

    @contrato(
        invariante=lambda self: self._value is not None and self._value != ""
    )
    def __init__(self, value):
        object.__setattr__(self, "_locked", False)
        object.__setattr__(self, "_value", value)
        object.__setattr__(self, "_locked", True)

    def __setattr__(self, key, value):
        if getattr(self, "_locked", False):
            raise AttributeError("EntityId é imutável")
        object.__setattr__(self, key, value)

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        if not isinstance(other, EntityId):
            return False
        return self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def __repr__(self):
        return f"EntityId({self._value!r})"