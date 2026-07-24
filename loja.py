import random
import time
import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

cl = "-"*140

print("Escolha sua Classe, Por Favor!")
classe = input('''Mago / Executor / Guerreiro / Arqueiro / Bandido
>> ''').lower()
print(cl)

while classe not in ["mago", "executor", "guerreiro", "arqueiro", "bandido"]:
    print("Resposta Inválida! Tente Novamente!")
    classe = input('''Mago / Executor / Guerreiro / Arqueiro / Bandido
>> ''').lower()
    print(cl)
    
print("Classe Escolhida:", classe.capitalize())

reais = 100000

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
verde1 = "\033[92m"
cinza = "\033[90m"

qtd = 0
bombas = 0
flechas = 0

def loja():

    global qtd, bombas, flechas, reais, classe

    PRECO_POCAO = 50
    PRECO_BOMBA = 150
    PRECO_FLECHA = 5

    while True:

        limpar()

        print(cl)
        print(f"{amarelo}=========== LOJA DA GUILDA ==========={branco}")
        print(f"Dinheiro : {amarelo}R${reais}{branco}")
        print("--------------------------------------")
        print(f"{verde}Poções : {qtd}{branco}")
        print(f"{roxo}Bombas : {bombas}{branco}")

        if classe == "arqueiro":
            print(f"{azul}Flechas: {flechas}{branco}")

        print(cl)

        print("1 - 🧪 Comprar Poções   (R$50)")
        print("2 - 💣 Comprar Bombas   (R$150)")

        if classe == "arqueiro":
            print("3 - 🏹 Comprar Flechas (R$5)")

        elif classe == "bandido":
            print(f"{vermelho}3 - 🗡️ Roubar Item{branco}")

        print("0 - Sair")

        try:
            escolha = int(input("\n>> "))
        except ValueError:
            print("Digite um número válido!")
            input("\nENTER...")
            continue

        # ==========================
        # SAIR
        # ==========================

        if escolha == 0:
            break

        # ==========================
        # POÇÕES
        # ==========================

        elif escolha == 1:

            try:
                comprar = int(input("\nQuantidade:\n>> "))
            except ValueError:
                print("Digite um número válido!")
                input("\nENTER...")
                continue

            if comprar <= 0:
                print("Quantidade inválida!")

            else:

                custo = comprar * PRECO_POCAO

                if custo > reais:
                    print("Dinheiro insuficiente!")

                else:
                    reais -= custo
                    qtd += comprar

                    print(f"\nVocê comprou {comprar} poções!")

        # ==========================
        # BOMBAS
        # ==========================

        elif escolha == 2:

            try:
                comprar = int(input("\nQuantidade:\n>> "))
            except ValueError:
                print("Digite um número válido!")
                input("\nENTER...")
                continue

            if comprar <= 0:
                print("Quantidade inválida!")

            else:

                custo = comprar * PRECO_BOMBA

                if custo > reais:
                    print("Dinheiro insuficiente!")

                else:
                    reais -= custo
                    bombas += comprar

                    print(f"\nVocê comprou {comprar} bombas!")

        # ==========================
        # FLECHAS
        # ==========================

        elif escolha == 3 and classe == "arqueiro":

            try:
                comprar = int(input("\nQuantidade:\n>> "))
            except ValueError:
                print("Digite um número válido!")
                input("\nENTER...")
                continue

            if comprar <= 0:
                print("Quantidade inválida!")

            else:

                custo = comprar * PRECO_FLECHA

                if custo > reais:
                    print("Dinheiro insuficiente!")

                else:
                    reais -= custo
                    flechas += comprar

                    print(f"\nVocê comprou {comprar} flechas!")

        # ==========================
        # BANDIDO
        # ==========================

        elif escolha == 3 and classe == "bandido":

            print(cl)
            print("O que deseja roubar?")
            print("1 - 🧪 Poção")
            print("2 - 💣 Bomba")

            roubo = input("\n>> ")

            chance = random.randint(1,100)

            print("\nTentando roubar...")
            time.sleep(2)

            if roubo == "1":

                if chance <= 75:

                    ganho = random.randint(1,5)
                    qtd += ganho

                    print(f"Você roubou {ganho} poções!")

                else:

                    multa = 150

                    print("O comerciante percebeu o roubo!")
                    print(f"Você perdeu R${multa}.")

                    reais = max(0, reais - multa)

            elif roubo == "2":

                if chance <= 45:

                    ganho = random.randint(1,3)
                    bombas += ganho

                    print(f"Você roubou {ganho} bombas!")

                else:

                    multa = 300

                    print("O comerciante percebeu o roubo!")
                    print(f"Você perdeu R${multa}.")

                    reais = max(0, reais - multa)

            else:
                print("Opção inválida!")

        else:
            print("Opção inválida!")

        input("\nENTER para continuar...")

    limpar()

    print(cl)
    print("INVENTÁRIO")

    print(f"🧪 Poções : {qtd}")
    print(f"💣 Bombas : {bombas}")

    if classe == "arqueiro":
        print(f"🏹 Flechas: {flechas}")

    print()

    if classe == "guerreiro":
        print("⚔️ Espada de Ferro")

    elif classe == "executor":
        print("🪓 Machado de Batalha")

    elif classe == "mago":
        print("🪄 Cajado de Madeira")

    elif classe == "arqueiro":
        print("🏹 Arco de Madeira")

    elif classe == "bandido":
        print("🗡️ Adaga Enferrujada")

    input("\nENTER para continuar...")

loja()