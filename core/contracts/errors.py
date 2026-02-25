class ContratoVioladoError(Exception):
    pass

class PreCondicaoVioladaError(ContratoVioladoError):
    pass

class PosCondicaoVioladaError(ContratoVioladoError):
    pass

class InvarianteVioladaError(ContratoVioladoError):
    pass
