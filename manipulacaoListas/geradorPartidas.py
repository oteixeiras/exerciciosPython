from funcoesGeradordePartidas import *

time = []
adversario = []
jogo = []
golsCampeonato = []

print("Olá, seja bem-vindo! \nComo deseja adicionar o placar dos jogos em cada rodada do campeonato? (1/2)")
resposta = int(input(("1- Adicionar manualmente\n2- Adicionar de forma aleatória\n => ")))

if resposta == 1:
    entradaManual(time, adversario, jogo, golsCampeonato)
else:
    print("Gerando placares aleatórios...")
    entradaAutomatica(time, adversario, jogo, golsCampeonato)

print("\nColeção dos resultado dos jogos: ", jogo)
print("a Pontuação final do time dentro do campeonato:", apuradorRodadas(time, adversario))
