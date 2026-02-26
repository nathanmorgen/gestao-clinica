from dataclasses import dataclass
from datetime import datetime, UTC
from typing import Dict, Any

@dataclass(frozen=True)
class EventoContrato:
    timestamp: str
    classe: str
    metodo: str
    tipo: str
    mensagem: str
    estado: Dict[str, Any]

    @staticmethod
    def agora(**kwargs):
        return EventoContrato(
            timestamp = datetime.now(UTC).isoformat(),
            **kwargs
        )
