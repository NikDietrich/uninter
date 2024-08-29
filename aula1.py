#exemplo de cálculos financeiros para empresa
faturamento = 1200  # tipo: int -> número inteiro
custo = 750.0 # tipo: float -> número com casa decimal
novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento
 
print("Faturamento foi de: ", faturamento)
print("Custo foi de: ", custo)
print("imposto foi de: ", imposto)
print("a margem de lucro foi de: ", round(margem_lucro, 3))

mensagem = "O faturamento da loja foi yyy" 
email = "emailteste@gmail.com" # tipo string -> texto
teve_lucro = True # tipo boolean -> verdadeiro ou falso

# mod -> % é o resto da divisão
tempo_contrato = 170
tempo_anos = 170/12
print("tempo em anos é: ", int(tempo_anos))
tempo_meses = 170 % 12
print ("tempo em meses é: ", tempo_meses)