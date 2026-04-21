#!/usr/bin/env python3
"""
devlife.py - Um dia na vida de um programador
Uso: python3 devlife.py
"""
import random
import time


def digitar(texto, v=0.025):
    for c in texto:
        print(c, end="", flush=True)
        time.sleep(v)
    print()


problemas = [
    "NullPointerException às 3h da manhã",
    "Bug que só acontece em producao (na sua maquina funciona)",
    "Codigo legado escrito em 2003 sem comentarios",
    "Senior pediu pra reescrever tudo no review",
    "Deploy na sexta-feira as 17h59",
    "Cliente pediu 'so uma mudancinha'",
    "Stack Overflow fora do ar",
]

solucoes = [
    "Tentar de novo",
    "Reiniciar o computador",
    "Comentar a linha que da erro",
    "git push --force (ninguem vai notar)",
    "Culpar o cache",
    "Mandar pro estagiario",
    "Copiar do Stack Overflow SEM LER",
    "Colocar try/except Exception: pass",
]

desculpas = [
    "Na minha maquina funciona! 🤷",
    "Isso nao e bug, e feature.",
    "Esta no backlog.",
    "Quem escreveu isso nao trabalha mais aqui... (era eu)",
    "A culpa e do DNS.",
    "Precisa limpar o cache.",
    "Funciona intermitentemente.",
]

print("=" * 50)
print("   📋  SIMULADOR DE DIA DO DEVELOPER")
print("=" * 50)
time.sleep(0.8)

digitar("\n🌅 09:00 - Abrindo o laptop...")
time.sleep(0.3)
digitar("☕  Passando o primeiro cafe...")
time.sleep(0.3)
digitar(f"💻 Abrindo a IDE... ({random.randint(45, 180)}s de load)")
time.sleep(0.6)

digitar(f"\n🚨 PROBLEMA DO DIA: {random.choice(problemas)}")
time.sleep(0.6)
digitar(f"💡 Solucao aplicada: {random.choice(solucoes)}")
time.sleep(0.6)
digitar(f'🗣  Standup amanha: "{random.choice(desculpas)}"')
time.sleep(0.6)

horas = random.randint(2, 6)
cafes = random.randint(4, 12)
bugs_novos = random.randint(3, 15)

print("\n" + "=" * 50)
print("📊 RELATORIO DO DIA:")
print(f"   ⏰  Horas extras: {horas}h")
print(f"   ☕  Cafes consumidos: {cafes}")
print(f"   🐛  Bugs resolvidos: 1")
print(f"   🪲  Bugs novos criados: {bugs_novos}")
print(f"   📈  Produtividade: {random.randint(-50, 15)}%")
print("=" * 50)
print("\n😴 Ate amanha. Mesmo bug, mesma hora.\n")
