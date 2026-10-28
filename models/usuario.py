from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError


class Usuario:
    _hasher = PasswordHasher()

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha_hash = self._hash_senha(senha)

    @classmethod
    def _hash_senha(cls, senha):
        return cls._hasher.hash(senha)

    def alterar_senha(self, nova_senha):
        self.__senha_hash = self._hash_senha(nova_senha)

    def validar_senha(self, senha):
        try:
            self._hasher.verify(self.__senha_hash, senha)
        except (VerificationError, InvalidHashError):
            return False

        if self._hasher.check_needs_rehash(self.__senha_hash):
            self.__senha_hash = self._hash_senha(senha)
        return True
