import pytest

from core.entity_id import EntityId
from core.contracts.errors import InvarianteVioladaError


# ---------------------------------------------------------------------
# ESPECIFICAÇÃO: EntityId é um Value Object de identidade semântica
# ---------------------------------------------------------------------


def test_cria_entity_id_valido():
    """
    Dado um valor não vazio
    Quando um EntityId é criado
    Então a identidade é válida e preservada
    """
    eid = EntityId("consulta-123")

    assert eid.value == "consulta-123"


def test_entity_id_nao_aceita_none():
    """
    Um EntityId nunca pode encapsular None
    """
    with pytest.raises(InvarianteVioladaError):
        EntityId(None)


def test_entity_id_nao_aceita_string_vazia():
    """
    Um EntityId nunca pode encapsular valor vazio
    """
    with pytest.raises(InvarianteVioladaError):
        EntityId("")


def test_entity_id_compara_por_valor():
    """
    EntityId possui igualdade semântica por valor,
    não por identidade de objeto
    """
    id1 = EntityId("abc")
    id2 = EntityId("abc")
    id3 = EntityId("def")

    assert id1 == id2
    assert id1 != id3


def test_entity_id_pode_ser_usado_em_sets_e_dicts():
    """
    EntityId deve ser hashable e seguro para uso em estruturas
    baseadas em hashing
    """
    ids = {EntityId("x"), EntityId("y")}

    assert EntityId("x") in ids
    assert EntityId("z") not in ids


def test_entity_id_e_imutavel():
    """
    Após criado, o valor de um EntityId não pode ser alterado
    """
    eid = EntityId("imutavel")

    with pytest.raises(AttributeError):
        eid._value = "outro"