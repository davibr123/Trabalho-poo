from .emprestimos import Emprestimo
from .livros import Livro
from .usuarios import Usuario


def executar() -> None:
    usuario = Usuario("Ana", "U001")
    livro = Livro("Dom Casmurro", "Machado de Assis", "L001")
    print("Início:", livro)

    emprestimo = Emprestimo(livro, usuario)
    print(f"Empréstimo ativo={emprestimo.ativo} | {livro}")

    emprestimo.devolver()
    print(f"Devolvido ativo={emprestimo.ativo} | {livro}")


if __name__ == "__main__":
    executar()