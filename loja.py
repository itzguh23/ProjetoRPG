import random
import time

bencao = random.randint(1, 100)
nome = "gustavo"

if bencao >= 0:
    print("Você ouve Passos pesados se aproximando...")
    time.sleep(3)
    print("Todos Presentes na Guilda paralisam e ficam em Silêncio...")
    time.sleep(3)
    print('''um Homem, Idoso, Aparenta ter 80+ anos, com uma longa Barba Branca e um Cajado de Madeira
Entra no estabelecimento...''')
    print()
    print("Ele se aproxima de Você...")
    print("Olá " + nome.capitalize() + ", Me chamo Merlin")
    time.sleep(3)
    print("como eu sei o seu Nome? voce Pergunta...")
    time.sleep(3)
    print("Eu sou um dos 5 Anciões Divinos, e eu sei de tudo que acontece nesse mundo...")
    time.sleep(3)
    print("Os Deuses me Enviaram para te Ajudar, Afinal Você é o Escolhido, O Héroi da Lenda!...")
    time.sleep(3)
    print("Aqui Receba Isso...")
    time.sleep(3)
    print("Sistema: Você Recebeu um Poder Divino, Ao Beber a Poção, você se Sente mais Forte...")
    time.sleep(3)
    print("Merlin: Preciso ir Agora, Até mais... Herói...")
    print()
    print("Seus Status Mudaram")

    input("\nAperte ENTER Para Continuar: ")

    hp = nível * 70
    mana = nível * 105
    reais = nível * 150

    print(f"{azul}Hp: {hp}")
    print(f"{verde1}Mana: {mana}")
    print(f"{amarelo}Dinheiro: {reais}{branco}")
    print(f"Idade Atual: {idade}")
    print(cl)