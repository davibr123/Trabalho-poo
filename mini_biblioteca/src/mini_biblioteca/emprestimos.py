from .livros import Livro
from .usuarios import Usuario


class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError(f"O livro '{livro.titulo}' já está emprestado.")
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        self.livro.disponivel = False

    def devolver(self) -> None:
        self.ativo = False
        self.livro.disponivel = True