class Medico:
    def __init__(self, id, nome, especialidade):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade

    def __eq__(self, outro):
        return isinstance(outro, Medico) and self.id == outro.id

    def __hash__(self):
        return hash(self.id)
