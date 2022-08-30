# -----------------------------------------------------
# Augusto Teixeira
# ATP Setembro/2020
# -----------------------------------------------------
# SISTEMA DE UMA LOJA
# -----------------------------------------------------


# Biblioteca para obter data atual
from datetime import datetime


def obter_limite():
    """Funcao para obter dados do cliente e calcular limite de gasto"""

    # MENSAGENS INICIAIS

    # Mensagem de boas-vindas
    print()
    print(f"Seja bem-vindo à loja {nome_loja}!"
          f" Aqui quem fala é {nome_lojista}.")

    print("----------------------")

    # Mensagem de análise de crédito
    print()
    print("A partir de agora, faremos uma análise de crédito para você!"
          "\nPor favor, informe os dados solicitados abaixo.")

    # DADOS DO CLIENTE

    # Cargo
    print()
    cargo_cliente = str(input("Cargo na empresa em que trabalha atualmente: "))

    # Salário
    # Inserção e validação de tipo
    salario_cliente = input("Salário (##.##): R$ ")
    salario_cliente = check_float(salario_cliente)

    # Validação de salário
    while salario_cliente <= 0.0:
        print("\n! AVISO !"
              "\nVocê inseriu um salário inválido.")
        print()

        salario_cliente = input("Por favor, insira novamente: ")

        # Execução de função de validação
        salario_cliente = check_float(salario_cliente)

    # Ano de nascimento
    # Inserção e validação de tipo
    ano_nascimento_cliente = input("Ano de nascimento: ")
    ano_nascimento_cliente = check_int(ano_nascimento_cliente)

    # Validação de ano
    while ano_nascimento_cliente > agora.year:
        print("\n! AVISO !"
              "\nVocê inseriu um ano futuro de nascimento.")
        print()

        ano_nascimento_cliente = input("Por favor, insira novamente: ")

        # Execução de função de validação
        ano_nascimento_cliente = check_int(ano_nascimento_cliente)

    print("----------------------")

    # Exibição de dados inseridos
    print()
    print(f"Você informou que seu cargo é {cargo_cliente},"
          f" seu salário é R$ {salario_cliente:.2f}"
          f" e você nasceu em {ano_nascimento_cliente}.")

    # IDADE E LIMITE DE GASTO

    # Cálculos + exibição
    print()
    global idade_cliente
    idade_cliente = agora.year - ano_nascimento_cliente
    limite_cliente = float((salario_cliente * (idade_cliente / 1000)) + 100)
    print(f"Você tem aproximadamente {idade_cliente} anos de idade"
          f" e poderá gastar até R$ {limite_cliente:.2f} em nossa loja!")

    print("----------------------")

    return limite_cliente


def verificar_produto(limite_cliente):
    """Funcao para cadastrar produtos e avaliar credito"""

    # DADOS DO PRODUTO

    # Mensagem de produto
    print()
    print("Por favor, informe abaixo os dados do produto que você deseja.")

    # Nome
    print()
    nome_produto = str(input("Nome do produto: "))

    # Preço
    # Inserção e validação de tipo
    preco_produto = input("Preço do produto (##.##): R$ ")
    preco_produto = check_float(preco_produto)

    # AVALIAÇÃO DE CRÉDITO

    compra_aprovada = True
    print()

    # Preço até 60% do limite do cliente
    if preco_produto <= (limite_cliente * (60 / 100)):
        print("Liberado!")

    # Preço maior que 60% e até 90% do limite do cliente
    elif preco_produto <= (limite_cliente * (90 / 100)):
        print("Liberado ao parcelar em até 2 vezes.")

    # Preço maior que 90% e até 100% do limite do cliente
    elif preco_produto <= limite_cliente:
        print("Liberado ao parcelar em 3 ou mais vezes.")

    # Preço maior que 100% do limite do cliente
    else:
        compra_aprovada = False
        print("Bloqueado.")

    # AVALIAÇÃO DE DESCONTO

    # Valor do produto entre:
    # -> "Quantidade de caracteres do nome completo do lojista" e "Idade do cliente"
    global idade_cliente
    if compra_aprovada:
        if len(nome_lojista) < preco_produto < idade_cliente:
            nome_lojista_termos = nome_lojista.rsplit(" ")
            primeiro_nome_lojista = nome_lojista_termos[0]
            desconto = len(primeiro_nome_lojista)
            preco_final = preco_produto - desconto

            print()
            print("PROMOÇÃO!"
                  f"\nVocê terá um desconto de R$ {desconto},00 no produto!"
                  f"\nO novo valor é R$ {preco_final:.2f}")
        else:
            print()
            print("Não há desconto para essa compra.")

    print()
    print("----------------------")


def check_int(valor):
    """Funcao para validar se o usuário está inserindo um número inteiro positivo"""

    while not str.isdigit(valor):
        aviso_valor()
        valor = input("Por favor, insira novamente: ")
    return int(valor)


def check_float(valor):
    """Funcao para validar se o usuário está inserindo um número decimal positivo"""

    # Remove o "." para saber se contém apenas números
    valor_sem_ponto = valor.replace('.', '', 1)

    # Assume que o valor não contem "."
    valor_contem_ponto = False
    qtd_pontos = 0

    while True:
        # Procura por "."
        while not valor_contem_ponto and qtd_pontos != 1:
            for item in valor:
                if item == ".":
                    valor_contem_ponto = True
                    qtd_pontos += 1

            # Valida se há apenas um "."
            if valor_contem_ponto and qtd_pontos == 1:
                break

            # Se não foi encontrado nenhum ou mais de um "."
            aviso_valor()
            valor = input("Por favor, insira novamente: ")

            # Atualiza as variáveis para a nova inserção
            valor_sem_ponto = valor.replace('.', '', 1)
            valor_contem_ponto = False
            qtd_pontos = 0

        # Valida se há apenas números além do "."
        while not valor_sem_ponto.isdigit():
            aviso_valor()
            valor = input("Por favor, insira novamente: ")
            valor_sem_ponto = valor.replace('.', '', 1)
            valor_contem_ponto = False
            qtd_pontos = 0

        # Se há apenas números além do "." e um único "."
        if valor_sem_ponto.isdigit() and qtd_pontos == 1:
            break

    return float(valor)


def aviso_valor():
    """Funcao para exibir mensagem padrão para erro de tipo"""

    print("\n! AVISO !"
          "\nVocê inseriu um tipo de dado inesperado para esse campo.")
    print()


# -----------------------------------------------------
# Estrutura principal do programa
# -----------------------------------------------------

agora = datetime.now()
nome_lojista = "Augusto César Souza Teixeira"
nome_loja = "XPTO"
idade_cliente = 0

# Execução de função
limite = obter_limite()

# Solicitação de quantidade para cadastro
print()
qtd_produtos = int(input("Digite a quantidade de produtos que você deseja cadastrar: "))

# Execução recursiva de função
for id_produto in range(qtd_produtos):
    verificar_produto(limite)

# Caso não deseje cadastrar nenhum produto
if qtd_produtos == 0:
    print("----------------------")

# Mensagem de encerramento
print()
print("Obrigado por utilizar nossa loja!")
