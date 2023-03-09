import random
import time
from array import *
import numpy as np
import pandas as pd

#Arrays, com gols_m sendo os marcados e s os sofridos
timesarr = []
pontos = []
gols_m = []
gols_s = []
primeiros_colocados = []

# Variáveis dos Loops
# atraso = 0.0002
i = 0
j = 0
k = 1
h = 0
y = 0
timesmam = 2


print("futibas simulator")
print("Quer simular o Brasileirão ou não?\nSe sim, digite s, se não, digite n e faça sua copa.")
while True:
    s_n2 = input()
    try:
        if s_n2 == "s":
            timesarr = ["Internacional", "Grêmio", "Santos","São Paulo","Corinthians","Palmeiras","Flamengo","Vasco","Fluminense","Botafogo","Athlético-PR", "Coritiba", "Cruzeiro", "Atlético-MG", "Goiás","Cuiabá","Fortaleza","Bragantino","Bahia","América-MG"]
            pontos = [0] * 20
            gols_m = [0] * 20
            gols_s = [0] * 20

        elif s_n2 == 'n':
            print("Certo, sua copa!")
        else:
            print("Digite s ou n")
            continue
        break
    except ValueError:
        print("Escolha um número natural, por favor")

if s_n2 == "n":
    print("Quantos times você quer em seu campeonato?")

    while True:
        times = input()
        try:
            val = int(times)
            print("O número de times será ", val)
            break
        except ValueError:
            print("Escolha um número natural, por favor")

    print("Vai querer que haja uma segunda fase em mata-mata?\nSe sim, digite s e quantos times da fase de grupo passaram, se não, digite n.")
    while True:
        s_n = input()
        try:
            if s_n == "s":
                print("Certo! Haverá um mata-mata")
                timesmam = int(input("Quantos times? "))
                print("O número de times no mata-mata será de:", timesmam)
            elif s_n == 'n':
                print("Certo, sem mata-mata")
            else:
                print("Digite s ou n")
                continue
            break
        except ValueError:
            print("Escolha um número natural, por favor")


    partidas = [[] for _ in range(val)]

    while y < val:
        print("Escolha seu time " + str(y+1))
        timesarr.append(str(input()))
        gols_m.append(0)
        gols_s.append(0)
        pontos.append(0)
        y += 1

    print("O campeonato foi criado! Vamos simular os jogos de todos contra todos!")
    print("Ok, o jogo será entre: ")
else:
    val = 20
    partidas = [[] for _ in range(val)]


# Loop para percorrer os times do array "timesarr"
# for time1 in timesarr:
    # Loop para percorrer os times do array "timesarr" também
    # for time2 in timesarr:
        # Imprime a partida entre os times correspondentes
        #if time1 != time2:
           # print(f"{time1} x {time2}")

while j < (val-1):
    p = 1
    while k < (val):
        if k > j:
            
            print("Ok, o jogo será entre: ")
            print(timesarr[j] + " vs " + timesarr[k])

            gols1 = 0
            gols2 = 0

            print("começou the game")

            # Faz o jogo, com os gols de cada time.
            while i <= 90:
                gay = random.randint(1,150)
                if(gay > 6):
                    print(i)
                elif(gay > 3):
                    print(str(i) + " gol do " + timesarr[j] + "!")
                    gols1 += 1
                elif(gay > 0):
                    print(str(i) + " gol do " + timesarr[k] + "!")
                    gols2 += 1
                i += 1
                #time.sleep(atraso)

            print("o game acabou pai, lols")
            print("o jogo terminou:")
            print(timesarr[j] + " " + str(gols1))
            print(" vs ")
            print(timesarr[k] + " " + str(gols2))

            # Soma os gols nas arrays para a tabela
            gols_m[j] += gols1
            gols_s[j] += gols2
            gols_m[k] += gols2
            gols_s[k] += gols1


            # Dá os pontos para o times
            if gols1 > gols2:
                pontos[j] += 3
            elif gols1 == gols2:
                pontos[j] += 1
                pontos[k] += 1
            else: 
                pontos[k] += 3
            
            partidas[j].append(f"Rodada {len(partidas[j])+1}: {timesarr[j]} {gols1} vs {gols2} {timesarr[k]}")
            partidas[k].append(f"Rodada {len(partidas[k])+1}: {timesarr[k]} {gols2} vs {gols1} {timesarr[j]}")
            print("Dê enter para ir ao próximo jogo")
            #nada = input()
            i = 0
            p +=1
        k += 1
    k=1
    j+=1

while h < (val):
    print(f"O time {timesarr[h]} fez {pontos[h]} pontos, marcou {gols_m[h]} gols, sofreu {gols_s[h]} gols e seu saldo de gols foi de " + str({gols_m[h]-gols_s[h]}))
    h += 1


dados = {
    "Nomes": timesarr,
    "Pontos": pontos,
    "Gols Marcados": gols_m,
    "Gols Sofridos": gols_s,
}

df = pd.DataFrame(dados)
df["Saldo de Gols"] = df["Gols Marcados"] - df["Gols Sofridos"]

# Classificar o DataFrame pela coluna de pontos em ordem decrescente
df = df.sort_values(["Pontos", "Saldo de Gols", "Gols Marcados"], ascending=[False, False, False])

# Remover o índice atual e definir um novo índice que consiste apenas em números sequenciais
df = df.reset_index(drop=True)
df.index +=1

# Imprimir o DataFrame classificado com as posições corretas e o contador na primeira coluna
print(df)

#Tentar fazer o mata-mata
# Selecionando os primeiros times
top_ = df.head(timesmam)

# Imprimindo o nome dos times
print("\nOs dois primeiros colocados")
print(top_['Nomes'])

if timesmam > 0:
    w = 0
    while w < timesmam:
        primeiros_colocados.append(df.iloc[w]['Nomes'])
        w += 1

    print(primeiros_colocados)



while True:
    print("Para ver os resultados de cada rodada de um time, digite o número do time e dê enter")
    while True:
        yay = input()
        try:
            e = int(yay)
            print('\n'.join(partidas[e-1]))
            break
        except ValueError:
            print("Escolha um número natural, por favor")
        except IndexError:
            print("Não há um time com esse local")
    print("Quer fechar o programa?")
    sair = input("s para sair, se não, só dê enter")
    if sair == "s":
        break
