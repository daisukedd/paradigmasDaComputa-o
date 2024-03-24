# Duas equipes de volei com no máximo 5 sets, cada set com no máximo 25 pontos, exceto o último que será disputado até 15 pontos.
# A equipe que vencer 3 sets vence a partida.
# Implemente um programa que leia o número de sets vencidos por cada equipe e determine o resultado da partida.
# O programa deve exibir a mensagem "Equipe 1 venceu" ou "Equipe 2 venceu" conforme o resultado da partida.
# Se o número de sets vencidos por ambas as equipes for igual, exiba a mensagem "Empate".



# Solicitar a pontuação da equipe A e equipe B
pontuacao_equipe_a = int(input("Pontuação da equipe A: "))
pontuacao_equipe_b = int(input("Pontuação da equipe B: "))

# Verificar o resultado da partida
if pontuacao_equipe_a > pontuacao_equipe_b:
    print("Equipe 1 venceu")
elif pontuacao_equipe_b > pontuacao_equipe_a:
    print("Equipe 2 venceu")
else:
    print("Empate")