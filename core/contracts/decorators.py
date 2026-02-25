from .events import EventoContrato
from .errors import (
    PreCondicaoVioladaError,
    PosCondicaoVioladaError,
    InvarianteVioladaError
)

def contrato(*, pre=None, pos=None, invariante=None, observador=None):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
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

            resultado = func(self, *args, **kwargs)

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

            return resultado
        return wrapper
    return decorator
