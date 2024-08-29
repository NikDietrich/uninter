#Listas produtos
list_produtos = ["iphone", "ipad", "airpod", "macbook"]
list_preco = [4000, 1000, 2000, 10000]
# Juntar as listas em um dicionário
dic_produtos = {"iphone": 4000, "ipad": 1000, "airpod": 2000, "macbook": 10000}

print(dic_produtos)

# pegar um elemento
print(dic_produtos["iphone"])

# editar um elemento
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos)

# quantidade de itens
print(len(dic_produtos))

# retirar um item do dicionário
#dic_produtos.pop("airpod")
#print(dic_produtos)

# adicionar um item no dicionário
dic_produtos["apple watch"] = 2500
print(dic_produtos)

# verificar se um item existe dentro de um dicionário
if "iphone" in dic_produtos:
    print("Existe produto")
else:
    print("não existe")

# verificar se um valor existe 
if 10000 in dic_produtos.values():
    print("Existe valor")
else:
    print("não existe")

# exercício: 


nome_produto = input("Insira o nome do produto: ")
preco_produto = input("Insira o preço do produto: ")

# Cadastrar novo produto se não existir, se existir, atualizar
nome_produto = nome_produto.lower
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

#if nome_produto in dic_produtos:
#    dic_produtos[nome_produto] = preco_produto
#else:
#    dic_produtos[nome_produto] = preco_produto
#print(dic_produtos)


# no final programa tem que atualizar todos os produtos para os novos valores (+10%)
# para 1 item:
produto = "airpod"

#novo_preco = dic_produtos[produto] * 1.1
#dic_produtos[produto] = novo_preco
#print(dic_produtos)

# para todos os produtos
for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco
print(dic_produtos)



