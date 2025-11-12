# ==========================================
# JOGO DA ADIVINHAÇÃO 🎯 
# Autor: Carlos Henrique 
# Descrição: O computador escolhe um número e o jogador tenta adivinhar.
# ==========================================

import random
import os

def limpar_tela():
    """Limpa o terminal (Windows ou Linux/macOS)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar():
    """Função principal do jogo."""
    limpar_tela()
    print("=" * 40)
    print(f"{'JOGO DA ADIVINHAÇÃO':^40}")
    print("=" * 40)

    # Gera um número aleatório entre 1 e 50
    numero_secreto = random.randint(1, 50)
    tentativas = 0

    print("\nTente adivinhar o número entre 1 e 50!")

    # Loop de palpites
    while True:
        try:
            palpite = int(input("\nSeu palpite: "))
            tentativas += 1
        except ValueError:
            print("⚠️ Digite apenas números!")
            continue

        if palpite < numero_secreto:
            print("🔼 Tente um número maior!")
        elif palpite > numero_secreto:
            print("🔽 Tente um número menor!")
        else:
            print(f"\n🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
            break

# Loop principal do programa (permite jogar várias vezes)
while True:
    jogar()
    print("\nDeseja jogar novamente?")
    resposta = input("Digite [S] para sim ou [N] para sair: ").strip().lower()
    if resposta != 's':
        print("\n👋 Obrigado por jogar! Até a próxima!")
        break
