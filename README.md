# 🎯 Jogo da Adivinhação em Python

Um jogo simples e divertido feito em **Python**, onde o computador escolhe um número aleatório e o jogador tenta adivinhar.  
A cada tentativa, o programa indica se o número é **maior** ou **menor** até o jogador acertar.  
Após vencer, é possível **jogar novamente** sem precisar reiniciar o código!

---

## 🚀 Funcionalidades

- O computador escolhe um número entre **1 e 50**.
- O jogador recebe dicas a cada palpite.
- Permite **repetir o jogo** quantas vezes quiser.
- Trata erros de entrada (caso o usuário digite algo que não seja número).
- Limpa a tela a cada nova partida para melhor visualização.

---

## 🧠 Conceitos aplicados

- Estruturas de repetição (`while`)
- Condições (`if`, `elif`, `else`)
- Funções (`def`)
- Geração de números aleatórios (`random`)
- Tratamento de erros com `try` e `except`
- Limpeza de terminal (`os.system`)

---

## 💡 Exemplo de uso

```bash
========================================
           JOGO DA ADIVINHAÇÃO
========================================
Tente adivinhar o número entre 1 e 50!

Seu palpite: 25
🔼 Tente um número maior!

Seu palpite: 37
🔽 Tente um número menor!

Seu palpite: 30
🎉 Parabéns! Você acertou o número 30 em 3 tentativas.
