from core.contracts.decorators import contrato


class IntervaloTempo:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

        # Invariante já validada na construção
        if not self._invariante():
            raise ValueError("Intervalo inválido: inicio deve ser menor que fim")

    # --------------------
    # Invariante estrutural
    # --------------------
    def _invariante(self):
        return self.inicio < self.fim

    # --------------------
    # Comportamentos
    # --------------------
    @contrato(
        pre=lambda self, outro: isinstance(outro, IntervaloTempo),
        pos=lambda self, resultado: isinstance(resultado, bool),
        invariante=lambda self: self._invariante(),
    )
    def sobrepoe(self, outro):
        return not (self.fim <= outro.inicio or outro.fim <= self.inicio)

    @contrato(
        pre=lambda self, instante: self.inicio <= instante < self.fim,
        pos=lambda self, resultado: isinstance(resultado, bool),
        invariante=lambda self: self._invariante(),
    )
    def contem(self, instante):
        return self.inicio <= instante < self.fim