import os
#biblioteca os pode mexer em arquivos, exemplo trocar nome:
# os.rename("nome antigo", "nome novo"), sendo nome antigo o caminho do arquivo, e o novo pra onde quer colocar

lista_arquivos = os.listdir("arquivos")
# os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt") - tira da arquivos e coloca na pasta 22
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
            print("Movimentar para a pasta 22")
        elif "23" in arquivo:
            print("Movimentar para a pasta 23")
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
   