import pytest

from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo
from core.entity_id import EntityId
from core.contracts.errors import PreCondicaoVioladaError


@pytest.fixture
def medico():
    return object()


@pytest.fixture
def paciente():
    return object()


@pytest.fixture
def sala():
    return object()


@pytest.fixture
def intervalo_valido():
    return IntervaloTempo(10, 20)


def test_consulta_rejeita_medico_nulo(paciente, sala, intervalo_valido):
    with pytest.raises(PreCondicaoVioladaError):
        Consulta(EntityId("c1"), None, paciente, sala, intervalo_valido)


def test_consulta_rejeita_paciente_nulo(medico, sala, intervalo_valido):
    with pytest.raises(PreCondicaoVioladaError):
        Consulta(EntityId("c2"), medico, None, sala, intervalo_valido)


def test_consulta_rejeita_sala_nula(medico, paciente, intervalo_valido):
    with pytest.raises(PreCondicaoVioladaError):
        Consulta(EntityId("c3"), medico, paciente, None, intervalo_valido)


def test_consulta_rejeita_intervalo_none(medico, paciente, sala):
    with pytest.raises(PreCondicaoVioladaError):
        Consulta(EntityId("c4"), medico, paciente, sala, None)


def test_consulta_rejeita_intervalo_tipo_invalido(medico, paciente, sala):
    with pytest.raises(PreCondicaoVioladaError):
        Consulta(EntityId("c5"), medico, paciente, sala, "10-11")


def test_consulta_criada_com_sucesso(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(EntityId("c6"), medico, paciente, sala, intervalo_valido)

    assert consulta.medico is medico
    assert consulta.paciente is paciente
    assert consulta.sala is sala
    assert consulta.intervalo is intervalo_valido