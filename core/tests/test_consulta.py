import pytest

from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo
from core.contracts.errors import ContratoVioladoError


class Dummy:
    pass


def test_consulta_valida_eh_criada():
    consulta = Consulta(
        medico=Dummy(),
        paciente=Dummy(),
        sala=Dummy(),
        intervalo=IntervaloTempo(10, 20),
    )

    assert consulta.medico is not None
    assert consulta.paciente is not None
    assert consulta.sala is not None
    assert consulta.intervalo is not None


def test_consulta_invalida_com_objetos_nulos():
    with pytest.raises(ContratoVioladoError):
        Consulta(
            medico=None,
            paciente=None,
            sala=None,
            intervalo=IntervaloTempo(10, 20),
        )


def test_consulta_invalida_com_intervalo_invalido():
    with pytest.raises(ContratoVioladoError):
        Consulta(
            medico=Dummy(),
            paciente=Dummy(),
            sala=Dummy(),
            intervalo=None,
        )


def test_validar_preserva_invariante():
    consulta = Consulta(
        medico=Dummy(),
        paciente=Dummy(),
        sala=Dummy(),
        intervalo=IntervaloTempo(10, 20),
    )

    # validar é um ponto semântico de contrato
    consulta.validar()

    assert consulta.medico is not None
    assert consulta.paciente is not None
    assert consulta.sala is not None
    assert isinstance(consulta.intervalo, IntervaloTempo)