class Sala:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __eq__(self, outro):
        return isinstance(outro, Sala) and self.id == outro.id

    def __hash__(self):
        return hash(self.id)
