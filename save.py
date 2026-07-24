bosshp = nível * 100
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")
poc_tu = 0
input("\nAperte ENTER Para Continuar: ")

while bosshp > 0 and hp > 0:
    poc_tu = 0
    limpar()
    print(f"A Vida dele está em: {roxo}{bosshp}{branco}")
    print(f"Sua Vida está em {azul}{int(hp)}{branco}")
    print()

# Opções de Luta

    luta = None
    
    def ler_input():
        global luta
        luta = input(f'''Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba / 5-Poção {vermelho}(VOCÊ TEM 10 SEGUNDOS PARA RESPONDER){branco}
>> ''')
        
    thread = threading.Thread(target=ler_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout=10)
    print()

# Luta = Atacar

    if luta == "1" and classe in ["guerreiro", "executor"]:

        bosshp, hp = ataque_corpo(bosshp, hp, nível, ataque_monstro)

    elif luta == "1" and classe == "mago":
        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print("Um Mago não é tão bom em Combate Corpo a Corpo, Tente Usar Magias!!!")
        print()
        print(cl)

    elif luta == "1" and classe == "arqueiro":
        
        bosshp, hp = ataque_tiro(bosshp, hp, nível, ataque_monstro)

# Luta = Magia

    elif luta == "3" and classe == "mago":
        bosshp, hp, mana = ataque_mago(bosshp, hp, nível, mana, ataque_monstro)

    elif luta == "3" and classe != "mago":

        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print("Apenas Magos podem usar Magias!")
        print()
        print(cl)

# Luta = Fugir

    elif luta == "2":
        hp = fuga_all(hp)

# Luta = Bomba

    elif luta == "4":
        bosshp, hp = ataque_bomba(bosshp, hp, nível, ataque_monstro)

# Luta = Poção

    elif luta == "5":

        if poc_tu >= 3:
            print("\nVocê já usou o limite de 3 poções neste turno!")
            print(cl)
            hp = ataque_monstro(bosshp, hp, nível)
            poc_tu = 0
        else:
            qtd, hp = usar_pocao(bosshp, hp, nível, qtd, ataque_monstro)
            poc_tu += 1
        
#Luta = Sem Resposta

    elif luta == None:
        print("\nVocê demorou muito tempo para Responder!")
        print("Você foi Penalizado!")
        pena = hp * 0.10
        hp -= pena
        print(f"Você perdeu {pena} de Vida!")
        print()

# Ação Inválida

    else:
        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print(f"Ação Inválida! Tente Novamente!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
        
# Final da Batalha
      
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