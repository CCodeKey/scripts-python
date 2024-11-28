from collections import Counter
from math import factorial

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def resultado(anagrama, repeticao):
    if repeticao == 0:
        print("    ##  Fórmula utilizada  ##")
        print(f"{BOLD}{RED}          P  = {GREEN} n{RED}! {RESET}")
        print()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print()
        print("Resultado da Permutação Simples ",anagrama,".")
    if repeticao >= 1:
        print("    ##  Fórmula utilizada  ##")
        print(f"{BLUE}           r {RESET}")
        print(f"{BOLD}{RED}          P  = {GREEN} n{RED}! {RESET}")
        print(f"{GREEN}           n   {BLUE} r! {RESET}")
        print()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print()
        print("- Resultado da Permutação Composta ",anagrama // repeticao,".")

def calcular_anagramas(palavra):
    n = len(palavra)
    anagrama = factorial(n)
    print(f"Nº de Anagramas    =  {n}! ou {anagrama}.")
    return anagrama

def calcular_repeticoes(frase):
    contador = Counter(frase)
    repeticoes = {letra: quantidade for letra, quantidade in contador.items() if quantidade > 1}
    return repeticoes

while True:
    print("    ##  Digite uma palavra  ##")
    palavra = input("> ")
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    repeticoes = calcular_repeticoes(palavra)
    num_anagramas = calcular_anagramas(palavra)
    num_repeticoes = sum(repeticoes.values())
    print(f"Nº de Repetições   =  {num_repeticoes}! ou {factorial(num_repeticoes)}.")
    num_repeticoes = factorial(num_repeticoes)
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    print("- Letras Repetidas :")
    num = 1
    for letra, quantidade in repeticoes.items():
        print(f"     {letra}: {quantidade} ou {factorial(quantidade)}!")
        num = num * factorial(quantidade)  
        print("num -> ", num)
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    resultado(num_anagramas , num)
    print()
    print()
    print()
    print()
