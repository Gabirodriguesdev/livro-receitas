import random

def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    computador = random.choice(opcoes)

    print("Bem-vindo ao Pedra, Papel e Tesoura!")
    jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

    if jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "Pedra" and computador == "Tesoura") or \
         (jogador == "Papel" and computador == "Pedra") or \
         (jogador == "Tesoura" and computador == "Papel"):
        print("Você venceu!")
    else:
        print("Computador venceu!")

jogar()