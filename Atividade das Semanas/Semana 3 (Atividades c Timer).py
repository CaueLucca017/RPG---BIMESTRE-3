# Atividade 1
num = [2, 5, 8, 9, 12, 15, 18]
resto = [n for n in num if n <= 15]
pares = [n for n in resto if n % 2 == 0]
quantidade_pares = len(pares)

print("Números até 15:", resto)
print("Números pares até 15:", pares)
print("Quantidade de pares:", quantidade_pares)


# Atividade 2
lista = [1, 2]

def soma(lista):
    total = 0
    for num in lista:
        total += num
    return total

print(soma(lista))


# Atividade 3
for i in range(5):
    print(i)


# Atividade 4
nomes = ["alice", "lucas", "bob"]
nomes_maiusculos = [nome.upper() for nome in nomes]
print(nomes_maiusculos)


# Atividade 5
palavras = ['gargantua', 'ciclope', 'aventureiros', 'python']
vogais = "aeiou"
total = 0

for palavra in palavras:        
    for letra in palavra:      
        if letra in vogais:    
            total += 1         

print('Total de vogais:', total)


# Atividade 6
import pandas as pd

dados = {
    "Nome": ["Arthur", "Lancelot", "Desconhecido", "Gawian"],
    "Moeda": [50, 30, 20, 0],
    "Classe": ["Cavaleiro", "Cavaleiro", "Cavaleiro", "Cavaleiro"]
}

df = pd.DataFrame(dados)
print(df)
