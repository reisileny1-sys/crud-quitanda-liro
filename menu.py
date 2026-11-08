import banco


def mostrar_produtos():
    produtos = banco.listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(
            f"{produto['id']:>3} | {produto['nome']:<25} | "
            f"{produto['categoria']:<25} | {produto['preco']} reais| {produto['unidade_medida']}"
        )


def cadastrar():
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = input("Preço do produto (R$): ")
    unidade_medida = input("Unidade de medida (L, mL, g, mg, kg): ")

    novo_id = banco.inserir_produto(nome, categoria, preco, unidade_medida)
    print(f"Produto cadastrado com id {novo_id}.")


def editar():
    produto_id = int(input("Id do produto: "))
    atual = banco.buscar_produto(produto_id)
    if atual is None:
        print("Produto nao encontrado.")
        return
    print("Enter vazio mantem o valor atual.")
    nome = input(f"Nome [{atual['nome']}]: ") or atual["nome"]
    categoria = input(f"Categoria [{atual['categoria']}]: ") or atual["categoria"]
    preco = input(f"Preço [{atual['preco']}]: ") or atual["preco"]
    unidade_medida = (
        input(f"Unidade de medida [{atual['unidade_medida']}]: ")
        or atual["unidade_medida"]
    )
    banco.atualizar_produto(produto_id, nome, categoria, preco, unidade_medida)
    print("Estudante atualizado.")


def excluir():
    produto_id = int(input("Id do produto: "))
    if banco.remover_produto(produto_id):
        print("Produto removido.")
    else:
        print("Porduto nao encontrado.")


def main():
    banco.criar_tabela()
    while True:
        print()
        print("1 - Listar   2 - Cadastrar   3 - Editar   4 - Excluir   0 - Sair")
        opcao = input("Opcao: ")
        if opcao == "1":
            mostrar_produtos()
        elif opcao == "2":
            cadastrar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            print("Ate logo.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
