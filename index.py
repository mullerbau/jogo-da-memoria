import random
import time
import os
from colorama import Fore, Back, Style


temp = '🐴🐴🐵🐵🐟🐟🐸🐸🐩🐩🦊🦊🐣🐣🐼🐼'
figuras = list(temp)

print("="*40)
print(" "*10 + "JOGO DA MEMORIA" + " "*10)
print("="*40)

jogador = input("Digite seu nome para jogar: ")

jogo = []
apostas = []

def preencherMatriz():
    
    for i in range(4):
        jogo.append([])
        apostas.append([])
        for _ in range(4):
            num = random.randint(0, len(figuras)-1)
            jogo[i].append(figuras[num])
            apostas[i].append('♦️')
            figuras.pop(num)
            
            
def mostraTabuleiro():
    os.system("cls")
    print("   1   2   3   4")
    for i in range(4):
        print(f'{i+1}', end="")
        for j in range(4):
            print(f" {jogo[i][j]} ", end="")
        print("\n")
        
    
    print("Memorize a posição dos bichos...")
    time.sleep(2)
    
    print("Contagem regressiva")
    for i in range(10, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(0.1)
        
    os.system("cls")
    
def mostraApostas():
    os.system("cls")
    print("   1   2   3   4")
    for i in range(4):
        print(f'{i+1}', end="")
        for j in range(4):
            print(f" {apostas[i][j]} ", end="")
        print("\n")
            
        
        
preencherMatriz()
mostraTabuleiro()

def fazAposta(num):
    while True:
        mostraApostas()
        posicao = input(f"{num} Coordenada (2 num, linha e coluna): ")
        if len(posicao) !=2:
            print("Informe uma dezena, por exemplo: 12, 21, 32...")
            time.sleep(2)
            continue
        x = int(posicao[0])-1
        y = int(posicao[1])-1
        try:
            if apostas[x][y] == "♦️":
                apostas[x][y] = jogo[x][y]
                break
            else:
                print("Coordenada já apostada... escolha outra")
                time.sleep(2)
        except IndexError:
            print("Coordenada inválida... repita")
            time.sleep(2)
    return x, y

def verificaTabuleiro():
    faltam = 0
    for i in range(4):
        for j in range(4):
            if apostas[i][j] == "♦️":
                faltam += 1
    return faltam

while True:             
    x1, y1 = fazAposta(1)
    x2, y2 = fazAposta(2)
    mostraApostas()
    
    if apostas[x1][y1] == apostas[x2][y2]:
        print("Parabéns! Você acertou! ")
        contador = verificaTabuleiro()
        totalPontos =+ 10
        if contador == 0:
            print("Parabéns você venceu!!!🏆🏆🏆")
            
            break
        else:
            print(f"Faltam {contador/2} bichos para descobrir")
    else:
        print("Errou... tente novamente.")
        time.sleep(2)
        totalPontos =- 5
        apostas[x1][y1] = "♦️"
        apostas[x2][y2] = "♦️"
        sair = input("Deseja sair (S/N): ").upper()
        if sair == "S":
            break
        
print("="*40)
print(" "*10 + f"Jogador: {jogador}" + " "*10)
print(" "*10 + f"Total de pontos: {totalPontos}" + " "*10)
print(" "*10 + f"Tempo de jogo: {tempo}" + " "*10)
print("="*40)


# Salvamento de dados
dados = []
if os.path.isfile("ranking.txt"):
    with open("ranking.txt", "r") as arq:
        dados = arq.readlines()
        
dados.append(f"{jogador};{totalPontos};\n")

with open("ranking.txt", "w") as arq:
    for dado in dados:
        arq.write(dado)
        
# Rotina para classificar  
nomes = []
pontos = []
tempo = []

for dado in dados:
    partes = dado.split(";")
    nomes.append(partes[0])
    pontos.append(int(partes[1]))
    tempos.append(int(partes[2])*-1)
    
    
# Coloca as 3 listas em ordem (zipando as 3 linhas)
juntas = sorted(zip(pontos, tempos, nomes), reverse=True)
# Volta a separar as listas (faz um "unzip")
pontos2, tempos2, nomes2 = zip(*juntas)

print()
print("="*43)
print("-----------< RANKING DOS JOGADORES: >------------")
print("="*43)
print("N° Nome do jogador.......: Pontos Tempo.:")

for num, (nome, ponto, tempo) in enumerate(zip(nomes2, pontos2, tempos2)):
    if nome == jogador and ponto == totalPontos:
        print(Fore.RED + f"{num:2d} {nome:25s}   {ponto:2d}   {tempo:3d}seg", end="")
        print(Style.RESET_ALL)
    else: 
        print(f"{num:2d} {nome:25s}   {ponto:2d}   {tempo:3d}seg", end="")
    
        
        
# -----------------EXERCÍCIO--------------------------
# 1. SOLICITAR NOME DO JOGADOR AO ENTRAR
# 2. DEFINIR PONTUAÇÃO (ACERTO +10, ERRO -5)
# 3. NO FINAL EXIBIR NOME E PONTUAÇÃO
# 4. ARMAZENAR HORA INICIAL E FINAL. EXIBIR TEMPO DE JOGO
# 5. SALVAR NOME, PONTUAÇÃO E TEMPO EM ARQUIVO TEXTO
# 6. MOSTRAR RANKING        