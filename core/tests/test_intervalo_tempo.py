import pytest
from core.contracts.errors import PreCondicaoVioladaError
from core.intervalo_tempo import IntervaloTempo


def test_criacao_intervalo_valido():
    intervalo = IntervaloTempo(10, 20)
    assert intervalo.inicio == 10
    assert intervalo.fim == 20


def test_intervalo_invalido_inicio_maior_ou_igual_fim():
    with pytest.raises(ValueError):
        IntervaloTempo(10, 10)

    with pytest.raises(ValueError):
        IntervaloTempo(20, 10)


def test_intervalos_nao_sobrepostos():
    a = IntervaloTempo(10, 20)
    b = IntervaloTempo(20, 30)
    c = IntervaloTempo(30, 40)

    assert not a.sobrepoe(b)
    assert not b.sobrepoe(c)
    assert not a.sobrepoe(c)


def test_intervalos_sobrepostos():
    a = IntervaloTempo(10, 30)
    b = IntervaloTempo(20, 40)
    c = IntervaloTempo(15, 25)

    assert a.sobrepoe(b)
    assert b.sobrepoe(a)
    assert a.sobrepoe(c)
    assert b.sobrepoe(c)


def test_contem_instante():
    intervalo = IntervaloTempo(10, 20)

    # Dentro do domínio válido
    assert intervalo.contem(10)
    assert intervalo.contem(15)

    # Fora do domínio válido → viola pré-condição
    with pytest.raises(PreCondicaoVioladaError):
        intervalo.contem(20)

    with pytest.raises(PreCondicaoVioladaError):
        intervalo.contem(25)