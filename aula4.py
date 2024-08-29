# if else e condições
vendas = 1500
meta = 1300

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

if vendas > meta:
    print("vendedor ganha bônus")
    bonus = 0.1 * vendas
    print("valor do bônus:", bonus)
else:
    print("vendedor não ganha bônus")

print( "Acabou o programa.")

# estabelecer mais de uma condição:

vendas = 500
meta1 = 1300 # ganha 10% de bonus
meta2 = 2000 # ganha 13% de bonus

if vendas >= meta2:
    bonus = 0.13 * vendas
else:
    if vendas >= meta1:
        bonus = 0.1 * vendas
    else:
        bonus = 0
    
    print("o bonus é de:", bonus)

# também da pra fazer usando o "ifelse"

if vendas >= meta2:
    bonus = 0.13 * vendas
elif vendas >= meta2:
    bonus = 0.1 * vendas
else:
    bonus= 0.5

print("o bonus é de:", bonus)

lista_produto = ["iphone","apple watch", "macbook", "airpods"]
nome_produto = input("insira o nome do produto: ")
nome_produto = nome_produto.lower()

if nome_produto in lista_produto:
    print("Produto em estoque")
else:
    print("sem estoque")