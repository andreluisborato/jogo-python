def batalha(vida=100, vida_oponente=50):
    print(f"Sua vida é {vida}")
    print(f"A vida do oponente é {vida_oponente}")
    print("Você começa! Escolha seu ataque:")
    print("1 - Soco")
    print("2 - Chute")
    print("3 - Tentar Fugir")
    ataque = input("Escolha: ")

    if ataque == "1":
        print("Você acertou um soco em cheio!")
        vida_oponente -= 20
        print(f"Sua vida: {vida}")
        print(f"Vida do oponente: {vida_oponente}")
    elif ataque == "2":
        print("Você deu um chute de raspão!")
        vida_oponente -= 5
        print(f"Sua vida: {vida}")
        print(f"Vida do oponente: {vida_oponente}")
    elif ataque == "3":
        print("Você tentou fugir... Mas ele foi mais rápido e te acertou!")
        vida -= 20
        print(f"Sua vida: {vida}")
        print(f"Vida do oponente: {vida_oponente}")

    if vida <= 0:
        print("Você foi derrotado!")
        return
    if vida_oponente <= 0:
        print("Você venceu a batalha!")
        return

    print("Vez do oponente!")
    print("1 - Esquivar")
    print("2 - Bloquear")
    print("3 - Fingir que vai atacar")
    escolha2 = input("Oque você faz? ")

    batalha(vida, vida_oponente)

def troca_poder():
    print("Deseja  trocar seu poder?")
    print("1- Sim")
    print("2 - Não")
    resposta1 = input("Escolha: ")

    if resposta1 == "1":
        print("Poderes:")
        print("1 - Colete")
        print("2 - Velocidade")
        print("3 - Bloqueio")
        poder = input("Digite o número do seu poder: ")

    elif resposta1 == "2":
        print("Você fica com seu poder... Mas terá que ser esperto!")
        batalha()


print("RPG")
nome = input("Qual seu nome: ")
print("Poderes:")
print("1 - Colete")
print("2 - Velocidade")
print("3 - Bloqueio")
poder = input("Digite o número do seu poder: ")

if poder == "1":
    print("Colete selecionado!")
elif poder == "2":
    print("Velocidade selecionada!")
elif poder == "3":
    print("Bloqueio selecionado!")

inventario = ["Espada", "Machado", "Baú", "Armadura"]
pergunta = input("Quer ver seu inventário? 1-Sim, 2-Depois: ")

if pergunta == "1":
    print(inventario)
elif pergunta == "2":
    print("Fechando inventário...")

print(f"{nome}, você está em uma floresta e ouve um barulho...")
print("Um ser desconhecido aparece das sombras!")
print("1 - Correr")
print("2 - Esperar")
escolha1 = input("Escolha: ")

if escolha1 == "1":
    print("Você escapou... Por enquanto!")

if escolha1 == "2" and poder == "3":
    print("Você bloqueou o ataque, agora terá que enfrentá-lo!")
    batalha()

if escolha1 == "2" and poder != "3":
    print("Seu poder não parou o ataque, boa sorte na próxima!")
    troca_poder()