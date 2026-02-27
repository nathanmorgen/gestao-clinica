import pytest
from core.consulta import Consulta
from core.intervalo_tempo import IntervaloTempo
from core.entity_id import EntityId

def test_consulta_exige_entity_id():
    intervalo = IntervaloTempo(10, 11)

    with pytest.raises(TypeError):
        Consulta(
            medico="Dr. A",
            paciente="Paciente X",
            sala="Sala 1",
            intervalo=intervalo
        )