from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario


def test_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis", "L001")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.codigo == "L001"
    assert livro.disponivel is True


def test_usuario():
    usuario = Usuario("Ana", "U001")
    assert usuario.nome == "Ana"
    assert usuario.id_usuario == "U001"


def test_emprestimo():
    livro = Livro("Dom Casmurro", "Machado de Assis", "L001")
    usuario = Usuario("Ana", "U001")
    emprestimo = Emprestimo(livro, usuario)
    assert emprestimo.livro is livro
    assert emprestimo.usuario is usuario
    assert emprestimo.ativo is True