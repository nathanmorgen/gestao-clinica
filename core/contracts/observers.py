import json
from pathlib import Path
from .events import EventoContrato

class ObservadorContrato:
    def registrar(self, evento: EventoContrato) -> None:
        raise NotImplementedError

class ObservadorJSON(ObservadorContrato):
    def __init__(self, arquivo: str):
        self._path = Path(arquivo)

    def registrar(self, evento: EventoContrato) -> None:
        with self._path.open("a", encoding="utf-8") as f:
            json.dump(evento.__dict__, f, ensure_ascii=False)
            f.write("\n")
