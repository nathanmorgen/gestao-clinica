import pytest

from core.agenda import Agenda
from core.intervalo_tempo import IntervaloTempo
from core.consulta import Consulta
from core.entity_id import EntityId
from core.medico import Medico
from core.paciente import Paciente
from core.sala import Sala
from core.contracts.errors import InvarianteVioladaError


def criar_consulta(
    consulta_id,
    medico_id,
    sala_id,
    inicio,
    fim,
):
    medico = Medico(id=medico_id, nome="Dr X", especialidade="Clínico")
    paciente = Paciente(id=1, nome="Paciente Y", contato="123")
    sala = Sala(id=sala_id, nome=f"Sala {sala_id}")
    intervalo = IntervaloTempo(inicio, fim)

    return Consulta(
        id=EntityId(consulta_id),
        medico=medico,
        paciente=paciente,
        sala=sala,
        intervalo=intervalo
    )


def test_inserir_consulta_sem_conflito():
    agenda = Agenda()

    c1 = criar_consulta(
        consulta_id="c1",
        medico_id=1,
        sala_id=1,
        inicio=10,
        fim=11
    )

    c2 = criar_consulta(
        consulta_id="c2",
        medico_id=2,
        sala_id=2,
        inicio=11,
        fim=12
    )

    agenda.inserir(c1)
    agenda.inserir(c2)

    assert len(agenda.consultas()) == 2


def test_conflito_de_medico_mesmo_intervalo():
    agenda = Agenda()

    c1 = criar_consulta(
        consulta_id="c1",
        medico_id=1,
        sala_id=1,
        inicio=10,
        fim=12
    )

    c2 = criar_consulta(
        consulta_id="c2",
        medico_id=1,  # mesmo médico
        sala_id=2,
        inicio=11,
        fim=13
    )

    agenda.inserir(c1)

    with pytest.raises(InvarianteVioladaError):
        agenda.inserir(c2)


def test_conflito_de_sala_mesmo_intervalo():
    agenda = Agenda()

    c1 = criar_consulta(
        consulta_id="c1",
        medico_id=1,
        sala_id=1,
        inicio=10,
        fim=12
    )

    c2 = criar_consulta(
        consulta_id="c2",
        medico_id=2,
        sala_id=1,  # mesma sala
        inicio=11,
        fim=13
    )

    agenda.inserir(c1)

    with pytest.raises(InvarianteVioladaError):
        agenda.inserir(c2)


def test_consultas_retorna_copia():
    agenda = Agenda()

    c1 = criar_consulta(
        consulta_id="c1",
        medico_id=1,
        sala_id=1,
        inicio=10,
        fim=11
    )

    agenda.inserir(c1)

    consultas = agenda.consultas()
    consultas.clear()

    # estado interno não deve ser afetado
    assert len(agenda.consultas()) == 1