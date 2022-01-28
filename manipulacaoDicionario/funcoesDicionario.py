def menu (resposta):

    print("<I> -Para Inserir um usuário\n")
    print("<P> -Para Pesquisar um usuário\n")
    print("<E> -Para Excluir um usuário\n")
    print("<L> -Para Listar um usuário\n")

    Resposta = input("O que deseja fazer: ").upper()

    return (resposta)

def inserir(usuario, quantidade):
    for aux in quantidade:
        usuarios[aux] = [input("qual o nome"),input("qual a data? "), input("qual a estação? ")]


