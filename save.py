import random
import time
import os

cl = "-"*140

# ===============================================================
# ====================== Cores do Terminal ======================
# ===============================================================

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
verde1 = "\033[92m"
cinza = "\033[90m"

lenda = int(input("Digite 1 para ser o Herói da Lenda ou 0 para ser Ninguém: "))
if lenda == 1:
    lenda = True
else:
    lenda = False
print()
idade = 16
nível = 1

def treinar():
    global nível, idade, hp, mana, reais
    while True:
        train = int(input('''Você é Novato, Precisa Treinar, Mas por quantos Anos?
>> '''))
        if train >= 2 and train <= 16:
            anos = train
            for i in range(anos):
                barra = "■" * (i + 1)
                __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
                aumento = 6
                nível += aumento
                time.sleep(0.3)

            print("\nDurante seu Treinamento, Você Subiu de Nível, Parabéns!!!")
            print(f"{azul}Novo Nível: {nível}{branco}")
            print("Esses são seus novos Status! ")
            input("\nAperte ENTER Para Continuar: ")
            print(cl)

            hp = nível * 50
            mana = nível * 75
            reais = nível * 100
            idade += anos

            print(f"{azul}Hp: {hp}")
            print(f"{verde1}Mana: {mana}")
            print(f"{amarelo}Dinheiro: {reais}{branco}")
            print(f"Idade Atual: {idade}")
            time.sleep(2)
            print(cl)
            input("\nAperte ENTER Para Continuar: ")
            break

        elif train <= 1:
            print("\nVocê precisa treinar por NO MÍNIMO, 2 Anos!")
            print()
            continue

        elif train >= 30:
            print("Você não precisa Treinar Tanto assim...")
            print()
            continue

        else:
            anos = train
            nível = 100
            for i in range(anos):
                barra = "■" * (i + 1)
                __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
                time.sleep(0.3)
            print("\nVocê treinou tanto, Que Alcançou o Nível 100(Máx)")
            print("Meus Parabéns!!!")
            print("Esses são seus novos Status! ")
            input("\nAperte ENTER Para Continuar: ")
            print(cl)

            hp = nível * 50
            mana = nível * 75
            reais = nível * 100
            idade += anos

            print(f"{azul}Hp: {hp}")
            print(f"{verde1}Mana: {mana}")
            print(f"{amarelo}Dinheiro: {reais}{branco}")
            print(f"Idade Atual: {idade}")
            time.sleep(2)
            print(cl)
            input("\nAperte ENTER Para Continuar: ")
            break
    return nível, idade, hp, mana, reais

def treinar_lenda():
    global nível, idade, hp, mana, reais
    while True:
        train = int(input('''Mesmo sendo o Herói da Profecia, Você precisa Treinar, Mas por quantos Anos?
>> '''))
        if train >= 2 and train <= 9:
            anos = train
            for i in range(anos):
                barra = "■" * (i + 1)
                __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
                aumento = 10
                nível += aumento
                time.sleep(0.3)

            print("\nDurante seu Treinamento, Você Subiu de Nível, Parabéns!!!")
            print(f"{azul}Novo Nível: {nível}{branco}")
            print("Esses são seus novos Status! ")
            input("\nAperte ENTER Para Continuar: ")
            print(cl)

            hp = nível * 70
            mana = nível * 100
            reais = nível * 150
            idade += anos

            print(f"{azul}Hp: {hp}")
            print(f"{verde1}Mana: {mana}")
            print(f"{amarelo}Dinheiro: {reais}{branco}")
            print(f"Idade Atual: {idade}")
            time.sleep(2)
            print(cl)
            input("\nAperte ENTER Para Continuar: ")
            break

        elif train <= 1:
            print("\nVocê precisa treinar por NO MÍNIMO, 2 Anos!")
            print()
            continue

        elif train >= 20:
            print("Você não precisa Treinar Tanto assim...")
            print()
            continue

        else:
            anos = train
            nível = 100
            for i in range(anos):
                barra = "■" * (i + 1)
                __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
                time.sleep(0.3)
            print("\nVocê treinou tanto, Que Alcançou o Nível 100(Máx)")
            print("Meus Parabéns!!!")
            print("Esses são seus novos Status! ")
            input("\nAperte ENTER Para Continuar: ")
            print(cl)

            hp = nível * 70
            mana = nível * 100
            reais = nível * 150
            idade += anos

            print(f"{azul}Hp: {hp}")
            print(f"{verde1}Mana: {mana}")
            print(f"{amarelo}Dinheiro: {reais}{branco}")
            print(f"Idade Atual: {idade}")
            time.sleep(2)
            print(cl)
            input("\nAperte ENTER Para Continuar: ")
            break
    return nível, idade, hp, mana, reais

if lenda == True:
    treinar_lenda()
else:
    treinar()

print(f"{azul}Hp: {hp}")
print(f"{verde1}Mana: {mana}")
print(f"{amarelo}Dinheiro: {reais}{branco}")
print(f"Idade Atual: {idade}")
print("Nível:", nível)