import pytest

from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo


# ─────────────────────────────────────────────
# Fixtures básicas
# ─────────────────────────────────────────────

@pytest.fixture
def intervalo_valido():
    return IntervaloTempo(10, 11)


@pytest.fixture
def medico():
    return object()


@pytest.fixture
def paciente():
    return object()


@pytest.fixture
def sala():
    return object()


# ─────────────────────────────────────────────
# Grupo A — Testes de PRÉ-CONDIÇÃO
# ─────────────────────────────────────────────

def test_consulta_rejeita_medico_nulo(paciente, sala, intervalo_valido):
    with pytest.raises(ValueError):
        Consulta(None, paciente, sala, intervalo_valido)


def test_consulta_rejeita_paciente_nulo(medico, sala, intervalo_valido):
    with pytest.raises(ValueError):
        Consulta(medico, None, sala, intervalo_valido)


def test_consulta_rejeita_sala_nula(medico, paciente, intervalo_valido):
    with pytest.raises(ValueError):
        Consulta(medico, paciente, None, intervalo_valido)


def test_consulta_rejeita_intervalo_none(medico, paciente, sala):
    with pytest.raises(TypeError):
        Consulta(medico, paciente, sala, None)


def test_consulta_rejeita_intervalo_tipo_invalido(medico, paciente, sala):
    with pytest.raises(TypeError):
        Consulta(medico, paciente, sala, "10-11")


# ─────────────────────────────────────────────
# Grupo B — Testes de PÓS-CONDIÇÃO
# ─────────────────────────────────────────────

def test_consulta_criada_com_sucesso(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta is not None


def test_consulta_atribui_medico_corretamente(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.medico is medico


def test_consulta_atribui_paciente_corretamente(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.paciente is paciente


def test_consulta_atribui_sala_corretamente(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.sala is sala


def test_consulta_atribui_intervalo_corretamente(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.intervalo is intervalo_valido


# ─────────────────────────────────────────────
# Grupo C — Testes de INVARIANTE
# ─────────────────────────────────────────────

def test_consulta_invariante_medico_nao_nulo(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.medico is not None


def test_consulta_invariante_paciente_nao_nulo(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.paciente is not None


def test_consulta_invariante_sala_nao_nula(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert consulta.sala is not None


def test_consulta_invariante_intervalo_tipo(medico, paciente, sala, intervalo_valido):
    consulta = Consulta(medico, paciente, sala, intervalo_valido)
    assert isinstance(consulta.intervalo, IntervaloTempo)