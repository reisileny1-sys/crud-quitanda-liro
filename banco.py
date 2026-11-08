import sqlite3

ARQUIVO_BANCO = "quitanda.db"


def conectar():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            nome   TEXT NOT NULL,
            categoria   TEXT NOT NULL,
            preco REAL NOT NULL,
            unidade_medida  TEXT NOT NULL
        )
        """)
    conexao.commit()
    conexao.close()


def inserir_produto(nome: str, categoria: str, preco: str, unidade_medida: str) -> int:
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO produtos (nome, categoria, preco, unidade_medida) VALUES (?, ?, ?, ?)",
        (nome, categoria, preco, unidade_medida),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id


# R — Read (todos)
def listar_produtos() -> list[dict]:
    conexao = conectar()
    linhas = conexao.execute("SELECT * FROM produtos ORDER BY id").fetchall()
    conexao.close()
    return [dict(linha) for linha in linhas]


# R — Read (um)
def buscar_produtos(produto_id: int) -> dict | None:
    conexao = conectar()
    linha = conexao.execute(
        "SELECT * FROM produtos WHERE id = ?", (produto_id,)
    ).fetchone()
    conexao.close()
    if linha is None:
        return None
    return dict(linha)


# U — Update
def atualizar_produto(
    produto_id: int, nome: str, categoria: str, preco: str, unidade_medida: str
) -> bool:
    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE produtos SET nome = ?, categoria = ?, preco = ?, unidade_medida = ?, WHERE id = ?",
        (nome, categoria, preco, unidade_medida, produto_id),
    )
    conexao.commit()
    alterou = cursor.rowcount > 0
    conexao.close()
    return alterou


# D — Delete
def remover_produto(produto_id: int) -> bool:
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conexao.commit()
    removeu = cursor.rowcount > 0
    conexao.close()
    return removeu
