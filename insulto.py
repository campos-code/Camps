#!/usr/bin/env python3
"""
insulto.py - Gerador de insultos carinhosos entre devs
Uso: python3 insulto.py
      python3 insulto.py 5      # gera 5 insultos
"""
import random
import sys


classicos = [
    "Seu codigo tem mais 'if' aninhado que cebola tem camada.",
    "Suas variaveis se chamam 'x', 'xx' e 'final_v2_USAR_ESSE.py'.",
    "Voce escreve codigo tao ruim que o linter pede demissao.",
    "Seu commit message e 'fix' e mudou 847 linhas.",
    "Voce coloca try/except Exception: pass e chama de 'robustez'.",
    "Voce testou em producao e chamou de QA.",
    "Seu git history parece o diario de uma pessoa em crise.",
    "Voce mistura tab e espaco no mesmo arquivo como um psicopata.",
    "Voce usa console.log pra debugar em producao.",
    "Seu README tem 2 linhas: 'TODO' e '(vazio de proposito)'.",
    "Voce abriu uma PR de 4000 linhas as 17h59 de sexta.",
    "Voce da merge em main sem rodar os testes... de novo.",
    "Voce tem 47 branches locais e nenhuma delas sabe mais pra que serve.",
    "Seu Dockerfile tem 'RUN apt-get update' e mais nada que funcione.",
    "Voce escreve comentarios explicando o QUE o codigo faz, nunca o PORQUE.",
    "Voce chama de 'refatoracao' quando na verdade reescreveu tudo do zero.",
    "Voce tem uma pasta chamada 'utils' com 3000 linhas de logica de negocio.",
    "Voce usa regex pra fazer parsing de HTML e dorme tranquilo.",
    "Voce commita node_modules 'so por garantia'.",
    "Voce esta programando desde 2010 e ainda usa 'var' em JavaScript.",
]

sujeitos = [
    "Seu codigo",
    "Sua PR",
    "Seu Dockerfile",
    "Seu yaml de CI",
    "Sua funcao de 400 linhas",
    "Seu commit",
    "Seu schema do banco",
    "Seu endpoint de API",
    "Seu Git history",
]

adjetivos = [
    "tao confuso",
    "tao bagunçado",
    "tao lento",
    "tao mal escrito",
    "tao ilegivel",
    "tao perigoso",
    "tao feio",
    "tao aleatorio",
    "tao desorganizado",
]

consequencias = [
    "que o Stack Overflow pede pra voce parar de perguntar.",
    "que o ChatGPT se recusa a ajudar.",
    "que o Git criou um branch novo so pra fugir.",
    "que o compilador mandou um pedido de socorro.",
    "que o servidor desligou sozinho de vergonha.",
    "que nem o autor original entende mais (voce, 2 semanas atras).",
    "que o linter virou ateu.",
    "que o code review virou terapia em grupo.",
    "que o CI ficou em 'pending' por 3 meses.",
    "que o estagiario pediu demissao so de olhar.",
]


def gerar_combinacao():
    return f"{random.choice(sujeitos)} e {random.choice(adjetivos)} {random.choice(consequencias)}"


def gerar_insulto():
    if random.random() < 0.6:
        return random.choice(classicos)
    return gerar_combinacao()


def main():
    n = 1
    if len(sys.argv) > 1:
        try:
            n = max(1, min(20, int(sys.argv[1])))
        except ValueError:
            n = 1

    print("🔥 " + "=" * 48)
    print("   INSULTOS CARINHOSOS DE DEV PRA DEV")
    print("=" * 50)
    for i in range(n):
        print(f"\n💬 {gerar_insulto()}")
    print("\n(com amor, do seu colega de trabalho ❤️)\n")


if __name__ == "__main__":
    main()
