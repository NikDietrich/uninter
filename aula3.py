# inputs -> interação com usuário, pegar infos
# email = input("Escreva o seu e-mail: ")
# nome = input("Escreva o seu nome: ")
# print(nome,email)

# print(f"{nome}, verifique seu e-mail: {email} que enviamos um link de confirmação.")

# faturamento= float(input("Digite seu faturamento anual: "))
# imposto = faturamento * 0.1

# print("O valor pago em imposto é: R$",imposto)


# listas

vendas = [100, 50, 14, 26, 700, 1]

# soma dos elementos

total_vendas = sum(vendas)
print(total_vendas)

# tamanho da lista
tamaho_lista = len(vendas)
print(tamaho_lista)

# max e min
maior_valor = max(vendas)
menor_valor = min(vendas)
print(maior_valor, menor_valor)

# pegar posição
print(vendas[0])

# exemplo de usabilidade

lista_produtos = ["iphone", "macbook", "airpods", "ipad"]

# busca_produto = busca_produto.lower() # padronizar os inputs
# busca_produto = input("pesquise pelo nome do produto: ")

# print(busca_produto in (lista_produtos))
# resultado ou é verdadeiro ou falso é booelan

# adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)


# remover um item
lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(0) # ele exclui o item que está na posição do parenteses
print(lista_produtos)

# editar um item
lista_precos = [1000, 1500, 3500]
lista_precos[0] = lista_precos[0] * 1.5 # substituir

# contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "macbook", "airpods", "ipad", "airpods", "airpods", "airpods", "iphone", "iphone"]
print(lista_produtos.count("iphone"))

# ordenar uma lista ordem alfabética ou crescente
lista_produtos.sort()
print(lista_produtos)
# ordenar uma lista ao contrário
lista_produtos.sort(reverse=True)
print(lista_produtos) 
