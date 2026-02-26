from core.contracts.snapshot import record_snapshot
from .events import EventoContrato
from .errors import (
    PreCondicaoVioladaError,
    PosCondicaoVioladaError,
    InvarianteVioladaError
)


def contrato(*, pre=None, pos=None, invariante=None, observador=None):
    def decorator(func):
        def wrapper(self, *args, **kwargs):

            # =====================
            # Pré-condição
            # =====================
            if pre and not pre(self, *args, **kwargs):
                evento = EventoContrato.agora(
                    classe=self.__class__.__name__,
                    metodo=func.__name__,
                    tipo="PRE",
                    mensagem="Pré-condição violada",
                    estado=self.__dict__.copy()
                )
                if observador:
                    observador.registrar(evento)
                raise PreCondicaoVioladaError(evento.mensagem)

            # =====================
            # Estado BEFORE
            # =====================
            state_before = {
                "classe": self.__class__.__name__,
                "metodo": func.__name__,
                "args": args,
                "kwargs": kwargs,
                "estado_objeto": self.__dict__.copy(),
            }

            # =====================
            # Execução
            # =====================
            resultado = func(self, *args, **kwargs)

            # =====================
            # Pós-condição
            # =====================
            if pos and not pos(self, resultado):
                evento = EventoContrato.agora(
                    classe=self.__class__.__name__,
                    metodo=func.__name__,
                    tipo="POS",
                    mensagem="Pós-condição violada",
                    estado=self.__dict__.copy()
                )
                if observador:
                    observador.registrar(evento)
                raise PosCondicaoVioladaError(evento.mensagem)

            # =====================
            # Invariante
            # =====================
            if invariante and not invariante(self):
                evento = EventoContrato.agora(
                    classe=self.__class__.__name__,
                    metodo=func.__name__,
                    tipo="INVARIANTE",
                    mensagem="Invariante violada",
                    estado=self.__dict__.copy()
                )
                if observador:
                    observador.registrar(evento)
                raise InvarianteVioladaError(evento.mensagem)

            # =====================
            # Estado AFTER
            # =====================
            state_after = {
                "resultado": resultado,
                "estado_objeto": self.__dict__.copy(),
            }

            # =====================
            # SNAPSHOT (somente se tudo foi válido)
            # =====================
            record_snapshot(
                function_name=f"{self.__class__.__name__}.{func.__name__}",
                state_before=state_before,
                state_after=state_after,
                metadata={
                    "tipo": "EXECUCAO_OK"
                }
            )

            return resultado

        return wrapper
    return decorator