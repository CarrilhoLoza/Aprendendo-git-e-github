#testando comandos git

#um codigo bem bobinho so pra usar de teste

nome = input("digite seu nome:")
duvida = input(f"Seu nome é {nome}?\n")

while True:
    if duvida.lower() == "sim":
        print("então ta bom")
        break
    elif duvida.lower() =='não' or duvida.lower()== "nao":
        print("eu acho que seu nome ta errado em")
        break
    else:
        print("so pode digitar sim ou não meu querido")
    duvida = input(f"sim ou não?\n")


    