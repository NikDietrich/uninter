faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f"faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

#editar texto:

email_cliente = "alalala@gmail.com"

# colocar tudo em maiúscula:
email_cliente = email_cliente.upper()
print(email_cliente)

# colocar tudo em minúscula:
email_cliente = email_cliente.lower()
print(email_cliente)

# buscar posição do caracter dentro da frase
print(email_cliente.find("@"))

# validar tamanho do texto
print(len(email_cliente))

# localizar um caracter por posição esquerda -> direita começando por 0
print(email_cliente[4])
# localizar um caracter por posição direita -> esquerda começando por -1
print(email_cliente[-2])

# pegar um trecho especifico do texto esquerda->direita, não contando o caracter em si
print(email_cliente[:4])
# pegar um trecho especifico do texto direita->esquerda, contando o caracter
print(email_cliente[4:])
# pegar um intervalo específico
print(email_cliente[1:6])

# substituir trecho de texto
novo_email = email_cliente.replace("gmail", "outlook")
print(novo_email)


# colocar 1ª letra maiúscula da primeira palavra apenas
nome = "nikolas dietrich"
print(nome.capitalize())
# colocar para todas as palavras
print(nome.title())

#pegar por exemplo só o servidor do e-mail
posicao_arroba = email_cliente.find("@")
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar separado primeiro e segundo nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[: posicao_espaco]
segundo_nome = nome [posicao_espaco+1:]
print(primeiro_nome)
print(segundo_nome)

# casos especiais - formatação numérica dentro do texto
margem_lucro = round(margem_lucro, 2)
print(f"faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem_lucro:.0%}")
