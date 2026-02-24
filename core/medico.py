class Medico:
    def __init__(self, id_, nome, especialidade):
        self.id = id_
        self.nome = nome
        self.especialidade = especialidade

    def __eq__(self, outro):
        return isinstance(outro, Medico) and self.id == outro.id

    def __hash__(self):
        return hash(self.id)
