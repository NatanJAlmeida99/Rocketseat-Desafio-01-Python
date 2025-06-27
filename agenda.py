def add_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso")
    return

def ver_lista_contato(contatos):
    print("\nLista de contatos: ")
    for index, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{index}. [{status}] {nome_contato} {telefone_contato} {email_contato}")
    return

def editar_contato(contatos, index_contato, novo_nome, novo_telefone, novo_email):
    if index_contato > 0:
        contatos[index_contato - 1]["nome"] = novo_nome
        contatos[index_contato - 1]["telefone"] = novo_telefone
        contatos[index_contato - 1]["email"] = novo_email
        print(f"Contato {index_contato} atualizado para {novo_nome} {novo_telefone} {novo_email}")
    else:
        print("Indice de tarefa inválido")

def favoritar_contato(contatos, index_contato):
    contatos[index_contato - 1]["favorito"] = True
    print(f"Contato {index_contato} marcado como favorito")
    return

def ver_lista_favoritos(contatos, contatos_favoritos):
    print("\nContatos Favoritos:")
    contatos_favoritos.clear()
    for contato in contatos:
        if contato["favorito"]:
            contatos_favoritos.append(contato)
    ver_lista_contato(contatos_favoritos)
    return

def apagar_contato(contatos, index):
    if 0 < index <= len(contatos):
        removido = contatos.pop(index - 1)
        print(f"Contato '{removido['nome']}' removido com sucesso.")
    else:
        print("Índice inválido.")

contatos = []
contatos_favoritos = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar Contato")
    print("2. Ver lista de Contatos")
    print("3. Editar Contato")
    print("4. Favoritar contato")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        nome_contato = str(input("Digite o nome do contato: "))
        nome_telefone = str(input("Digite o telefone do contato: "))
        nome_email = str(input("Digite o email do contato: "))
        add_contato(contatos, nome_contato, nome_telefone, nome_email)
    elif escolha == 2:
        ver_lista_contato(contatos)
    elif escolha == 3:
        ver_lista_contato(contatos)
        index_contato = int(input("Digite o número do contato que deseja editar: "))
        novo_nome = str(input("Digite o novo nome do contato: "))
        novo_telefone = str(input("Digite o novo telefone do contato: "))
        novo_email = str(input("Digite o novo email do contato: "))
        editar_contato(contatos, index_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == 4:
        ver_lista_contato(contatos)
        index = int(input("Digite o número do contato que deseja favorita: "))
        favoritar_contato(contatos, index)
    elif escolha == 5:
        ver_lista_favoritos(contatos, contatos_favoritos)
    elif escolha == 6:
        ver_lista_contato(contatos)
        index = int(input("Digite o número do contato que deseja apagar: "))
        apagar_contato(contatos, index)
    elif escolha == 7:
        break