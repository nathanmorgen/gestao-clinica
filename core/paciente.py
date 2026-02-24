class Paciente:
    def __init__(self, id_, nome, contato):
        self.id = id_
        self.nome = nome
        self.contato = contato

    def __eq__(self, outro):
        return isinstance(outro, Paciente) and self.id == outro.id

    def __hash__(self):
        return hash(self.id)
