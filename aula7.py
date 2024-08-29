lista_prcos = [1500, 1800, 2000, 3400]

#Imposto
# Aliquota1 - IR = 0.2
# Aliquota2 - ISS = 0.15
# Aliquota3 - CSLL = 0.05

#pra criar função, conforme abaixo

def calcula_imp_total(preco):
    if preco <= 2000:
        imposto_ir = preco * 0.2
    else:
        imposto_ir = preco * 0.3
    imposto_iss = preco*0.15
    imposto_csll = preco*0.05
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total
    
#criada a função, só substituir:


# preco = 1500
# imposto_ir = preco * 0.2
# imposto_total = imposto_ir + imposto_iss + imposto_csll
# imposto_iss = preco*0.15
# imposto_csll = preco*0.05
# print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}")


#for preco in lista_prcos:
#    imposto_ir = preco * 0.2
#    imposto_iss = preco*0.15
#    imposto_csll = preco*0.05
#    imposto_total = imposto_ir + imposto_iss + imposto_csll
#   print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}")  

#usando a função:
for preco in lista_prcos:
    imposto_total = calcula_imp_total (preco)
    print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}")

#agora se precisar fazer pra outra lista, vai precisar repetir todos os códigos
# inclusive se tiver alteração, vai ser necessário fazer em 1 por 1

nova_lista = [800, 2000, 1250, 3150] 

#for preco in nova_lista:
#    imposto_ir = preco * 0.2
#    imposto_iss = preco*0.15
#    imposto_csll = preco*0.05
#    imposto_total = imposto_ir + imposto_iss + imposto_csll
#    print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}") 

# usar a função em várias variáveis economiza tempo
for preco in nova_lista:
    imposto_total = calcula_imp_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}") 

#Se tiver condição em alguma alíquota, exemplo IR: 
# Aliquota1 - IR = 0.2 se valor até 2000, se maior é 0.3

nova_lista2 = [800, 2000, 1250, 3150] 

# for preco in nova_lista2:
#    if preco <= 2000:
#        imposto_ir = preco * 0.2
#    else:
#        imposto_ir = preco * 0.3
#    imposto_iss = preco*0.15
#    imposto_csll = preco*0.05
#   imposto_total = imposto_ir + imposto_iss + imposto_csll
#    print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}") 


# usando a função também

for preco in nova_lista2:
    imposto_total = calcula_imp_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco} é de: R${imposto_total}") 

