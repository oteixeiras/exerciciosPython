import random

def entradaManual(time, adversario, jogo, golsCampeonato):
    for aux in range(10):
        print("Rodada:",aux+1)
        time.append(input("Digite a quantidade de gols marcados pelo Time: "))
        adversario.append(input("Digite a quantidade de gols do time Adversário: "))
        print("~~~~~~~~~~~~~~~~~~")
        golsCampeonato = (time, adversario)

    for aux2 in range(10):
        jogo.append((golsCampeonato[0][aux2], golsCampeonato[1][aux2]))

def apuradorRodadas(x, y):
    vitoria = 0
    empate = 0
    derrota = 0

    for aux2 in range(10):
        if x[aux2] > y[aux2]:
            vitoria = (vitoria+1)
        elif x[aux2] < y[aux2]:
            derrota = (derrota+1)
        else:
            empate = (empate + 1)
    return ((vitoria*3) + empate)

def entradaAutomatica(time, adversario, jogo, golsCampeonato):
    for aux in range(10):
        time.append(random.randrange(0, 10, ))
        adversario.append(random.randrange(0, 10, ))
        golsCampeonato = (time, adversario)

    for aux2 in range(10):
        jogo.append((golsCampeonato[0][aux2], golsCampeonato[1][aux2]))

