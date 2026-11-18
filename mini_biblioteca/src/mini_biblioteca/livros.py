class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True

    def __str__(self) -> str:
        estado = "disponível" if self.disponivel else "indisponível"
        return f"{self.titulo} - {self.autor} [{self.codigo}] ({estado})"