from .usuario import Usuario


class Cliente(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
