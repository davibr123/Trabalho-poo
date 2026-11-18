import pytest

from mini_biblioteca.emprestimos import Emprestimo
from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario


@pytest.fixture
def livro():
    return Livro("Dom Casmurro", "Machado de Assis", "L001")


@pytest.fixture
def usuario():
    return Usuario("Ana", "U001")


def test_livro_novo_disponivel(livro):
    assert livro.disponivel is True


def test_emprestimo_torna_livro_indisponivel(livro, usuario):
    Emprestimo(livro, usuario)
    assert livro.disponivel is False


def test_nao_emprestar_livro_indisponivel(livro, usuario):
    Emprestimo(livro, usuario)
    with pytest.raises(ValueError):
        Emprestimo(livro, Usuario("Bruno", "U002"))


def test_devolver(livro, usuario):
    emprestimo = Emprestimo(livro, usuario)
    emprestimo.devolver()
    assert emprestimo.ativo is False
    assert livro.disponivel is True


def test_emprestar_novamente_apos_devolucao(livro, usuario):
    Emprestimo(livro, usuario).devolver()
    novo = Emprestimo(livro, usuario)
    assert novo.ativo is True