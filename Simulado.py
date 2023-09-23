import os
import time

produtos = [
    {"ID": 1, "nome": "Camisa", "preco": 20.00, "quantidade": 10, "categoria": "Vestuario"},
    {"ID": 2, "nome": "Tenis", "preco": 200.00, "quantidade": 2, "categoria": "Calcados"},
    {"ID": 3, "nome": "Blusa", "preco": 40.00, "quantidade": 2, "categoria": "Vestuario"},
    {"ID": 4, "nome": "Bone", "preco": 50.00, "quantidade": 1, "categoria": "Vestuario"},
    {"ID": 5, "nome": "Salto", "preco": 250.00, "quantidade": 2, "categoria": "Calcados"}
]


def tela():
    os.system("cls")
    print("            Gerenciador  de Estoque          ")
    print("1.Adicionar um novo produto ao inventário")
    print("2.Remover um produto do inventário usando o ID")
    print("3.Atualizar informações de um produto existente")
    print("4.Listar todos os produtos de uma categoria específica")
    print("5.Calcular o valor total em estoque")
    print("6.Encontrar produtos com quantidade abaixo de um determinado limite")
    print("7.Ranking produtos valiosos")
    print("8.Busca de produto por nome")
    opcao()


def opcao():
    opcao = int(input("Digite a opcao desejada: "))
    match opcao:
        case 1:
            nome = input("Digite o nome do produto: ")
            preco = int(input("Digite o preco do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            categoria = input("Digite a categoria do produto: ")
            add_produto(nome, preco, quantidade, categoria), time.sleep(2), tela()
        case 2:
            id = int(input("Digite o id do produto que deseja remover: "))
            delete_produto(id), time.sleep(2), tela()
        case 3:
            id = int(input("Digite o id do produto que deseja editar: "))
            edit_produto(id), time.sleep(5), tela()
        case 4:
            categoria = input("Digite a categoria que deseja listar: ")
            listar_produto_por_categoria(categoria), time.sleep(5), tela()
        case 5:
            calcular_estoque(), time.sleep(2), tela()
        case 6:
            quantidade = int(input("Digite qual quantidade deseja filtrar: "))
            find_produto_low_stock(quantidade), time.sleep(2), tela()
        case 7:
            ranking_produtos(), time.sleep(5), tela()
        case 8:
            nome = input("Digite o nome do produto que deseja buscar: ")
            find_por_nome(nome), time.sleep(5), tela()
        case _:
            print("Opcao invalida!")


def add_produto(nome, preco, quantidade, categoria):
    i = (len(produtos))
    novo_produto = {"id": i + 1, "nome": nome, "preco": preco, "quantidade": quantidade, "categoria": categoria}
    produtos.append(novo_produto)
    print("Produto adcionado com sucesso!")


def delete_produto(id):
    if id < (len(produtos)):
        for produto in produtos:
            if produto["ID"] == id:
                produtos.remove(produto)
                print("Produto deletado com sucesso!")
    else:
        print("ID invalido.")


def edit_produto(id):
    if id < (len(produtos)):
        for produto in produtos:
            if produto["ID"] == id:
                nome = input("Digite o nome do produto: ")
                preco = int(input("Digite o preco do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                categoria = input("Digite a categoria do produto: ")
                produto["nome"] = nome
                produto["preco"] = preco
                produto["quantidade"] = quantidade
                produto["categoria"] = categoria
                print("Produto editado com sucesso!")
    else:
        print("ID invalido.")
    print(produtos)


def listar_produto_por_categoria(categoria):
    produtos_encontrados = False
    for produto in produtos:
        if produto["categoria"] == categoria:
            print("ID:", produto["ID"], "Nome:", produto["nome"], "Preco:", produto["preco"], "Quantidade:",
                  produto["quantidade"])
            produtos_encontrados = True
    if produtos_encontrados == False:
        print("Nenhum produto encontrado.")


def calcular_estoque():
    valor = 0
    for produto in produtos:
        valor = valor + produto["preco"] * produto["quantidade"]
    print("Valor total do estoque:", valor)


def find_produto_low_stock(quantidade):
    produtos_encontrados = False
    for produto in produtos:
        if produto["quantidade"] <= quantidade:
            print("ID:", produto["ID"], "Nome:", produto["nome"], "Preco:", produto["preco"], "Quantidade:",
                  produto["quantidade"], "Categoria:", produto["categoria"])
            produtos_encontrados = True
    if produtos_encontrados == False:
        print("Nenhum produto encontrado.")


def ranking_produtos():
    produtos_ordenados = sorted(produtos, key=lambda produto: produto["quantidade"] * produto["preco"], reverse=True)
    for produto in produtos_ordenados:
        print("ID:", produto["ID"], "Nome:", produto["nome"], "Preco:", produto["preco"], "Quantidade:",
              produto["quantidade"], "Categoria:", produto["categoria"])


def find_por_nome(nome):
    produtos_encontrados = False
    for produto in produtos:
        if produto["nome"]== nome:
            print("ID:", produto["ID"], "Nome:", produto["nome"], "Preco:", produto["preco"], "Quantidade:",
                  produto["quantidade"], "Categoria:", produto["categoria"])
            produtos_encontrados = True
    if produtos_encontrados == False:
        print("Nenhum produto encontrado.")


tela()
