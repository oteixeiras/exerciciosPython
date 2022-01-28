from funcoesDicionario import*

usuarios = {}
resposta = menu()
while resposta == "I" or resposta == "P" or resposta == "E" or resposta == "L":
    if resposta == "I":
        quantidade = int(input("Qual a quantidade de inputs que deseja realizar? "))
        inserir(usuarios, quantidade)
    print(usuarios)
