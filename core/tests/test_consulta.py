import pytest

from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo


class Dummy:
    """Objeto mínimo para médico, paciente e sala."""
    pass


# -------------------------
# Testes de criação
# -------------------------

def test_consulta_valida_eh_criada():
    consulta = Consulta(
        medico=Dummy(),
        paciente=Dummy(),
        sala=Dummy(),
        intervalo=IntervaloTempo(10, 20)
    )

    assert consulta is not None


def test_consulta_invalida_com_objetos_nulos():
    with pytest.raises(ValueError):
        Consulta(
            medico=None,
            paciente=None,
            sala=None,
            intervalo=IntervaloTempo(10, 20)
        )


def test_consulta_invalida_com_intervalo_invalido():
    with pytest.raises(TypeError):
        Consulta(
            medico=Dummy(),
            paciente=Dummy(),
            sala=Dummy(),
            intervalo=None
        )


# -------------------------
# Testes de contrato
# -------------------------

def test_validar_preserva_invariante():
    consulta = Consulta(
        medico=Dummy(),
        paciente=Dummy(),
        sala=Dummy(),
        intervalo=IntervaloTempo(10, 20)
    )

    # método contratual não deve lançar erro
    consulta.validar()

    # estado permanece válido
    assert consulta.medico is not None
    assert consulta.paciente is not None
    assert consulta.sala is not None
    assert consulta.intervalo.inicio < consulta.intervalo.fim