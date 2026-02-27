class ContratoVioladoError(Exception):
    """
    Erro raiz para qualquer violação de Design by Contract.
    Deve ser usado como tipo semântico, nunca ValueError genérico.
    """
    pass


class PreCondicaoVioladaError(ContratoVioladoError):
    """
    Violação de pré-condição.
    Ocorre antes da execução do método.
    """
    pass


class PosCondicaoVioladaError(ContratoVioladoError):
    """
    Violação de pós-condição.
    Ocorre após a execução do método.
    """
    pass


class InvarianteVioladaError(ContratoVioladoError):
    """
    Violação de invariante estrutural do objeto.
    Pode ocorrer após qualquer operação pública.
    """
    pass