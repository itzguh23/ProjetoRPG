import random
import time
import os

cl = "-"*140
bencao = random.randint(1, 100)
if bencao >= 85:
    lenda = True
else:
    lenda = False

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

def input(*args, **kwargs):
    texto = " ".join(map(str, args))

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.03)
    
    return __builtins__.input()

def print(*args, **kwargs):

    texto = " ".join(map(str, args))

    if texto.startswith(cl):
        __builtins__.print(texto, **kwargs)
        return

    end = kwargs.get("end", "\n")

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.03)

    __builtins__.print(end=end)

def medo(*args, **kwargs):

    texto = " ".join(map(str, args))

    if texto.startswith(cl):
        __builtins__.print(texto, **kwargs)
        return

    end = kwargs.get("end", "\n")

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.2)

    __builtins__.print(end=end)

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

        print("1 - Comprar Poções   (R$50)")
        print("2 - Comprar Bombas   (R$150)")

        if classe == "arqueiro":
            print("3 - Comprar Flechas  (R$5)")

        elif classe == "bandido":
            print(f"{vermelho}3 - Roubar Item{branco}")

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
            print("1 - Poção")
            print("2 - Bomba")

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

    print(f"Poções : {qtd}")
    print(f"Bombas : {bombas}")

    if classe == "arqueiro":
        print(f"Flechas: {flechas}")

    if classe == "guerreiro":
        print("Espada de Ferro")

    elif classe == "executor":
        print("Machado de Batalha")

    elif classe == "mago":
        print("Cajado de Madeira")

    elif classe == "arqueiro":
        print("Arco de Madeira")

    elif classe == "bandido":
        print("Adaga Enferrujada")

    input("\nENTER para continuar...")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def heroi(hp, mana, reais):
    global nome, nível, idade, bencao

    print("Você sente uma Presença pesada se aproximando...")
    time.sleep(2)
    print("Todos Presentes na Guilda paralisam e ficam em Silêncio...")
    time.sleep(2)
    print('''um Homem, Idoso, Aparenta ter 80+ anos, com uma longa Barba Branca e um Cajado de Madeira, entra no estabelecimento...''')
    time.sleep(2)
    print("Ele se aproxima de Você...")
    time.sleep(2)
    print()
    medo(f"{vermelho}você está tomado pelo medo...")
    time.sleep(2)

    print()
    print(f"{verde}Merlin{branco}: Olá " + nome.capitalize() + ", Me chamo Merlin")
    time.sleep(2)
    print(f"{verde}Merlin{branco}: como eu sei o seu Nome? você Pergunta...")
    time.sleep(2)
    print(f"{verde}Merlin{branco}: Eu sou um dos 5 Anciões Divinos, e eu sei de tudo que acontece nesse mundo...")
    time.sleep(2)
    print(f"{verde1}Merlin{branco}: Os Deuses me Enviaram para te Ajudar, Afinal Você é o Escolhido, O Herói da Profecia!...")
    time.sleep(2)
    print(f"{verde}Merlin{branco}: Aqui Receba Isso...")
    time.sleep(2)
    print(f"{cinza}Sistema{branco}: Você Recebeu um Poder Divino, Ao Beber a Poção, você se Sente mais Forte...")
    time.sleep(2)
    print(f"{verde}Merlin{branco}: Preciso ir Agora, Até mais... Herói...")
    time.sleep(2)
    print()
    print("Seus Status Mudaram")

    input("\nAperte ENTER Para Continuar: ")
    
    hp = nível * 70
    mana = nível * 100
    reais = nível * 150

    print(f"{azul}Hp: {hp}")
    print(f"{verde1}Mana: {mana}")
    print(f"{amarelo}Dinheiro: {reais}{branco}")
    print(f"Idade Atual: {idade}")
    print(f"Classe: {classe.capitalize()}")
    print(f"{vermelho}HERÓI DA PROFECIA{branco}")
    print(cl)

    return hp, mana, reais

# ==================================================================
# ====================== Informações Iniciais ======================
# ==================================================================

print(cl)
nome = input(f'''{branco}Qual é o Seu Nome?
>> ''')
print(cl)

while True:
    idade = int(input('''Quantos anos Você Tem?
>> '''))
    print(cl)

    if idade < 14:
        print("\nVocê é Muito Novo(a) para Entrar na Guilda!")
        print(cl)
        continue
    
    elif idade > 40:
        print("\nVocê já está Muito Velho(a) para Entrar na Guilda")
        print(cl)
        continue

    else:
        break

print("Escolha sua Classe, Por Favor!")
classe = int(input('''1 - Mago / 2 - Executor / 3 - Guerreiro / 4 - Arqueiro / 5 - Bandido
>> '''))
print(cl)

while classe not in [1, 2, 3, 4, 5]:
    print("Resposta Inválida! Tente Novamente!")
    classe = int(input('''1 - Mago / 2 - Executor / 3 - Guerreiro / 4 - Arqueiro / 5 - Bandido
>> '''))
    print(cl)

if classe == 1:
    classe = "mago"
elif classe == 2:
    classe = "executor"
elif classe == 3:
    classe = "guerreiro"
elif classe == 4:
    classe = "arqueiro"
elif classe == 5:
    classe = "bandido"

print("Classe Escolhida:", classe.capitalize())

nível = 1
print(f"\nOlá {nome.capitalize()} Bem Vindo a Guilda dos Aventureiros, Você é um Novato(a) de nível:", nível)
print(cl)

print("Esses são seus Status Iniciais!")

input("\nAperte ENTER Para Continuar: ")

hp = nível * 50
mana = nível * 75
reais = nível * 100

print(f"{azul}Hp: {hp}")
print(f"{verde1}Mana: {mana}")
print(f"{amarelo}Dinheiro: {reais}{branco}")
print(f"Idade Atual: {idade}")
print(f"Classe: {classe.capitalize()}")
print(cl)

if lenda == True:
    heroi(hp, mana, reais)

# ===================================================================
# ====================== Treinamento de 3 Anos ======================
# ===================================================================

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
            print(f"Classe: {classe.capitalize()}")
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
            print(f"Classe: {classe.capitalize()}")
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
            print(f"Classe: {classe.capitalize()}")
            print(f"{vermelho}HERÓI DA PROFECIA{branco}")
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
            print(f"Classe: {classe.capitalize()}")
            print(f"{vermelho}HERÓI DA PROFECIA{branco}")
            time.sleep(2)
            print(cl)
            input("\nAperte ENTER Para Continuar: ")
            break
    return nível, idade, hp, mana, reais

if lenda == True:
    treinar_lenda()
else:
    treinar()

limpar()

loja()

# ===================================================================
# ====================== Definições da Batalha ======================
# ===================================================================


def ataque_monstro(bosshp ,hp, nível):
    cnt = random.randint(1, 10)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    time.sleep(1.5)
    if bosshp > 0:
        if cnt >= 9:
            print()
            print(f"o {roxo}Dragão{branco} tentou Contra-Atacar mas Você Desviou!")
            input("\nAperte ENTER Para Continuar: ")

        elif cnt >= 6:
            print()
            dn = nível * 5
            hp = hp - dn
            print(f"o {roxo}Dragão{branco} Contra-Atacou e pegou de Raspão!")
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")

        elif cnt >= 3:
            print()
            print(f"o {roxo}Dragão{branco} Contra-Atacou e por Pouco não pega em Cheio!")
            dn = nível * 15
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            

        else:
            print()
            print(f"O {roxo}Dragão{branco} Decidiu Contra-Atacar e Pegou em Cheio!")
            dn = nível * 25
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            
    return hp

def ataque_corpo(bosshp, hp, nível, ataque_monstro):

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    sorte = random.randint(1, 100)

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
            
    if sorte <= 20:
        print()
        print("Você errou o Ataque!!!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
            
    elif sorte >=21:
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 >= 14:
            dano = 10000
            bosshp = bosshp - dano
            print()
            print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
            print("Matando ele na Hora!!!")
            print()
            print(cl)

        elif d20 >= 10:
            dano = nível * 35
            bosshp = bosshp - dano
            print()
            print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif d20 >= 5:
            dano = nível * 25
            bosshp = bosshp - dano
            print()
            print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                    
        else:
            dano = nível * 10
            bosshp = bosshp - dano
            print()
            print("Você Desferiu um corte na Perna dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

def ataque_tiro(bosshp, hp, nível, ataque_monstro):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)
        
    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')

    if sorte <= 20:
        print()
        print("Você errou o Tiro!!!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
            
    elif sorte >=21:
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 >= 14:
            dano = 10000
            bosshp = bosshp - dano
            print()
            print(f"Você atirou uma Flecha que perfurou o Coração do {roxo}Dragão{branco}")
            print("Matando ele na Hora!!!")
            print()
            print(cl)

        elif d20 >= 10:
            dano = nível * 35
            bosshp = bosshp - dano
            print()
            print("Você atirou uma Flecha na Barriga dele! e ela entrou muito fundo!!!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif d20 >= 5:
            dano = nível * 25
            bosshp = bosshp - dano
            print()
            print("Você deu um tiro na cabeça dele, mas ele conseguiu desviar, o Tiro Acertou o rosto dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                    
        else:
            dano = nível * 10
            bosshp = bosshp - dano
            print()
            print("Você atirou uma Flecha na Perna dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

def ataque_mago(bosshp, hp, nível, mana, ataque_monstro):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''Você rolou um D100!
Número: {sorte}''')

    print()
    print("Escolha sua magia:")
    magia = input('''1-Bola de Fogo / 2-Telecinese / 3-Congelamento
>> ''').strip()

    print("\nProcessando magia...")
    time.sleep(1)
    print(cl)

    # ❌ Falha geral do ataque
    if sorte <= 10:
        print("Você errou a magia!")
        hp = ataque_monstro(bosshp, hp, nível)
        return bosshp, hp, mana

    # 🎲 ataque normal
    d20 = random.randint(1, 20)
    print(f"Você rolou um D20: {d20}")

    # =========================
    # 🔮 TELECINESE
    # =========================
    if magia == "2":

        if mana < 700:
            print("Mana insuficiente para Telecinese!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 >= 14:
            dano = 10000
            gasto = nível * 10

            bosshp -= dano
            mana -= gasto

            print(f"Você esmagou o Dragão com telecinese!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        elif d20 >= 10:
            dano = nível * 35
            gasto = nível * 7

            bosshp -= dano
            mana -= gasto

            print(f"Você prensou o Dragão com pedras!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("Sua telecinese falhou!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # 🔥 BOLA DE FOGO
    # =========================
    elif magia == "1":

        if mana < 550:
            print("Mana insuficiente para Bola de Fogo!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 >= 10:
            dano = nível * 25
            gasto = int(nível * 5.5)

            bosshp -= dano
            mana -= gasto

            print(f"Bola de fogo acertou o Dragão!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("Sua bola de fogo falhou!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # ❄ CONGELAMENTO
    # =========================
    elif magia == "3":

        if mana < 400:
            print("Mana insuficiente para Congelamento!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 == 1:
            dano = nível * 10
            gasto = nível * 4

            bosshp -= dano
            mana -= gasto

            print("Você congelou o Dragão parcialmente!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("O congelamento não foi eficaz!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # ❌ magia inválida
    # =========================
    else:
        print("Magia inválida!")
        hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp, mana

def fuga_all(hp):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
        
    if sorte <= 60:
        dano = 10000
        hp -= dano
        print()
        print(f"sua Tentativa de Fuga Falhou, o {roxo}Dragão{branco} te Matou!!!")
        
    elif sorte >=61:
        print()
        print(f"Você Fugiu do {roxo}Dragão {branco}com Sucesso!")
        print("Porém, O Vilarejo foi Destruído...")
        print(f"{vermelho}GAME OVER!{branco}")
        print()
        print(cl)
    return hp

def ataque_bomba(bosshp, hp, nível, ataque_monstro):
    sorte = random.randint(1, 100)
    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
        
    if sorte <= 30:

        bomba = 5
        while bomba > 0:
            print(bomba)
            bomba -= 1
            time.sleep(0.3)
        print("BOOM!!!")
        print("Você Errou a Bomba!")
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)

    elif sorte >=31:
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 <= 10:

            bomba = 5
            while bomba > 0:
                print(bomba)
                bomba -= 1
                time.sleep(0.3)
            dano = nível * 50
            bosshp = bosshp - dano
            print("BOOM!!!")
            print(f"Na hora que o {roxo}Dragão {branco}Abriu a Boca, Você lançou a Bomba na Garganta Dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif d20 >= 11:

            bomba = 5
            while bomba > 0:
                print(bomba)
                bomba -= 1
                time.sleep(0.3)
            dano = nível * 30
            bosshp = bosshp - dano
            print("BOOM!!!")
            print(f"Você lançou a Bomba no {roxo}Dragão{branco}, Machucou Muito!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

def usar_pocao(bosshp, hp, nível, qtd, ataque_monstro):
    hp_max = nível * 50

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    if qtd <= 0:
        print()
        print("Você Não tem Poções no Inventário!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)

    elif hp >= hp_max:
        print()
        print("Sua vida já está cheia! Não precisa usar Poção.")
        print()
        print(cl)

    else:
        porc = 0.10
        cura = hp_max * porc
        hp += cura

        if hp > hp_max:
            hp = hp_max

        qtd -= 1
        print()
        print(f"Você Bebeu uma {vermelho}Poção {branco}e Recuperou {int(cura)} de Vida!")
        print(f"{azul}Vida Atual: {int(hp)}{branco}")
        print()
        print(cl)

    return qtd, hp

def ataque_bandido(bosshp, hp, nível, ataque_monstro):

    print(cl)

    d20 = random.randint(1,20)

    print(f"Você rolou um D20!")
    print(f"Resultado: {d20}")

    if d20 == 20:

        dano = nível * 65

        print("✨ GOLPE FURTIVO CRÍTICO!")
        print(f"Você causou {dano} de dano!")

    elif d20 >= 16:

        dano = nível * 45

        print("Você acertou vários golpes rápidos!")

    elif d20 >= 11:

        dano = nível * 30

        print("Você acertou uma facada precisa!")

    elif d20 >= 2:

        dano = nível * 15

        print("Você acertou um golpe fraco.")

    else:

        dano = 0
        print("Você errou!")

    bosshp -= dano

    duplo = random.randint(1,100)

    if duplo <= 20:

        print()
        print(f"{amarelo}ATAQUE DUPLO!{branco}")

        dano2 = dano // 2

        bosshp -= dano2

        print(f"Você acertou uma segunda facada e causou {dano2} de dano!")

        if bosshp <= 0:
            return bosshp, hp

        print()

        print("O Dragão prepara um contra-ataque...")

        time.sleep(2)

        esquiva = random.randint(1,100)

        if esquiva <= 25:

            print(f"{verde}Você desviou do ataque do Dragão!{branco}")
            print("Nenhum dano recebido!")

    else:

        hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

# =====================================================================
# ====================== Batalha contra o Dragão ======================
# =====================================================================

def barra_vida(atual, maximo, tamanho=20):

    if atual < 0:
        atual = 0

    porcentagem = atual / maximo

    cheio = int(porcentagem * tamanho)

    vazio = tamanho - cheio

    barra = "█" * cheio + "░" * vazio

    return f"[{barra}] {int(atual)}/{int(maximo)} {branco}({porcentagem*100:.0f}%)"

bosshp = nível * 100
bosshp_max = bosshp
hp_max = hp
poc_tu = 0

while bosshp > 0 and hp > 0:

    limpar()

    print(cl)
    print(f"{roxo}══════ DRAGÃO ══════")
    print(barra_vida(bosshp, bosshp_max))
    print()

    print(f"{vermelho}══════ JOGADOR ══════")
    print(barra_vida(hp, hp_max) + branco)
    print(f"{verde}Mana: {mana}")
    print(f"{azul}Poções: {qtd}")
    print(f"{amarelo}Bombas: {bombas}")
    if classe == "arqueiro":
        print(f"{branco}Flechas: {flechas}")
    print()

    print(f"Escolha sua ação para atacar o {roxo}Dragão{branco}!")

    if classe == "guerreiro":
        print("1 - Espada")

    elif classe == "executor":
        print("1 - Machado")

    elif classe == "mago":
        print("1 - Magias")

    elif classe == "arqueiro":
        print("1 - Arco")

    elif classe == "bandido":
        print("1 - Adagas")
    
    print("2 - Bomba")
    print("3 - Poção")
    print("4 - Fugir")

    acao = input(">> ")

    if acao == "1":

        if classe in ["guerreiro","executor"]:

            bosshp, hp = ataque_corpo(
                bosshp,
                hp,
                nível,
                ataque_monstro
            )

        elif classe == "mago":

            bosshp, hp, mana = ataque_mago(
                bosshp,
                hp,
                nível,
                mana,
                ataque_monstro
            )

        elif classe == "arqueiro":

            if flechas <= 0:

                print("Você está sem flechas!")

                hp = ataque_monstro(
                    bosshp,
                    hp,
                    nível
                )

            else:

                flechas -= 1

                bosshp, hp = ataque_tiro(
                    bosshp,
                    hp,
                    nível,
                    ataque_monstro
                )

        elif classe == "bandido":

            bosshp, hp = ataque_bandido(
                bosshp,
                hp,
                nível,
                ataque_monstro
            )

    elif acao == "2":

        if bombas <= 0:

            print("Você não possui bombas!")

            hp = ataque_monstro(
                bosshp,
                hp,
                nível
            )

        else:

            bombas -= 1

            bosshp, hp = ataque_bomba(
                bosshp,
                hp,
                nível,
                ataque_monstro
            )

    elif acao == "3":

        if poc_tu >= 3:

            print("Você já usou 3 poções neste turno!")

            hp = ataque_monstro(
                bosshp,
                hp,
                nível
            )

        else:

            qtd, hp = usar_pocao(
                bosshp,
                hp,
                nível,
                qtd,
                ataque_monstro
            )

            poc_tu += 1

    elif acao == "4":

        hp = fuga_all(hp)
        break

    else:

        print("Ação inválida!")

        hp = ataque_monstro(
            bosshp,
            hp,
            nível
        )

# ==============================================================
# ====================== Final da Batalha ======================
# ==============================================================
   
if bosshp <= 0:
    print()
    print(f"O {roxo}Dragão {branco}está Morto, Você salvou o Vilarejo!!!")
    print()
    print(f"{verde}Povo do Vilarejo:{branco} MUITO OBRIGADO {nome.upper()} VOCÊ NOS SALVOU, PEGUE ISSO COMO RECOMPENSA")
    input("\nAperte ENTER Para Continuar: ")
        
    win = 10000
    reais += win
    print()

    print(f"{amarelo}{win} Reais{branco} Adicionados ao Banco")
    print()

    print(f"Seu saldo Agora é:{amarelo}", round(reais, 2), "Reais")
    print(branco)
    print(cl)

elif hp <= 0:
    print()
    print("Você está Morto!!!")
    print(f"{vermelho}GAME OVER!{branco}")
    print()
    print(cl)