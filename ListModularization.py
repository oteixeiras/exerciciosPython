# programa desenvolvido em Python 3.6.1 por Fernando de Souza Teixeira

# importando biblioteca para utilizar geração dos placares aleatórios
import random

# opção para Coletar os resultados de cada partida de foma manual (gols de cada time) - input do usuário
def entradaManual(time, adversario, jogo, golsCampeonato):

    for aux in range(10):
        print("Rodada:",aux+1)
        time.append(input("Digite a quantidade de gols marcados pelo Time: "))
        adversario.append(input("Digite a quantidade de gols do time Adversário: "))
        print("~~~~~~~~~~~~~~~~~~")
        golsCampeonato = (time, adversario)

    # gerando coleção dos placares de cada rodada - gols do time e do adversário por partida
    for aux2 in range(10):
        jogo.append((golsCampeonato[0][aux2], golsCampeonato[1][aux2]))

# contabiliza Vitórias, derrotas e empates entre os 2 times dentro de cada rodada
def apuradorRodadas(x, y):
    vitoria = 0
    empate = 0
    derrota = 0

    # identificado se o time ganhou, perdeu ou empatou dentro de cada partida, além de contabilizar de forma quantitativa os mesmos
    for aux2 in range(10):
        if x[aux2] > y[aux2]:
            vitoria = (vitoria+1)
        elif x[aux2] < y[aux2]:
            derrota = (derrota+1)
        else:
            empate = (empate + 1)
    # retornando a pontuação final do time dentro do campeonato (vit = +3 ponto, der = 0 e emp= +1)
    return ((vitoria*3) + empate)

# resultado das partidas de forma automática
def entradaAutomatica(time, adversario, jogo, golsCampeonato):

    # gerando de forma aleatória (0 a 10) os gols marcados pelo dois times ao longo das 10 rodadas
    for aux in range(10):
        time.append(random.randrange(0, 10, ))
        adversario.append(random.randrange(0, 10, ))
        golsCampeonato = (time, adversario)

    # gerando coleção dos placares de cada rodada - gols do time e do adversário por partida
    for aux2 in range(10):
        jogo.append((golsCampeonato[0][aux2], golsCampeonato[1][aux2]))

# entrada inicial dos dados e centralização das funções
def main():
    time = []
    adversario = []
    jogo = []
    golsCampeonato = []

    print("Olá, seja bem-vindo! \nComo deseja adicionar o placar dos jogos em cada rodada do campeonato? (1/2)")
    resposta = int(input(("1- Adicionar manualmente\n2- Adicionar de forma aleatória\n => ")))
    # gerando os placares de forma manual
    if resposta == 1:
        entradaManual(time, adversario, jogo, golsCampeonato)
    # gerando os placares de forma automática
    else:
        print("Gerando placares aleatórios...")
        entradaAutomatica(time, adversario, jogo, golsCampeonato)
    # retorno para o usuário
    print("\nColeção dos resultado dos jogos: ", jogo)
    print("a Pontuação final do time dentro do campeonato:", apuradorRodadas(time, adversario))

# chamando a função principal após ter carregado todas as demais, assim podendo iniciar o programa
main()
