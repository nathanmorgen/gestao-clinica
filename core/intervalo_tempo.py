class IntervaloTempo:
    def __init__(self, inicio, fim):
        if inicio >= fim:
            raise ValueError("Intervalo inválido: inicio deve ser menor que fim")
        self.inicio = inicio
        self.fim = fim

    def sobrepoe(self, outro):
        return not (self.fim <= outro.inicio or outro.fim <= self.inicio)

    def contem(self, instante):
        return self.inicio <= instante < self.fim
