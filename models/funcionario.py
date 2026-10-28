from .usuario import Usuario


class Funcionario(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
