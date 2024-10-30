"""
Resolução da avaliação prática 1 da UC "Inteligência Artificial" - Universidade da Beira Interior, Departamento de Informática
Realizada por João Miguel Santos a50367 - LEI
https://github.com/jmiguelsantos2047

-----------------------------------------------------------------------------------------------------------------------------
Pretendemos um programa que consiga jogar uma variante do jogo do galo usando a estratégia
da poda alfa-beta. O caso vencedor seria fazer um "L" com 3 símbolos, em vez da tradicional linha/coluna/diagonal.
O tabuleiro também é reduzido a 8 posições, eliminando o canto superior direito.
Todos os algoritmos/excertos de código usados estão devidamente documentados!
Vamos representar um estado por uma lista com 8 posições, em que cada
posição pode valer 1 se estiver ocupada pelo jogador MAX, -1 se estiver
ocupada pelo jogador MIN e 0 se estiver vazia.
As nove posições representam as casas do jogo do galo de acordo com o
seguinte esquema:
0 1
2 3 4
5 6 7

As ações de um jogador são representadas pelo número inteiro correspondente
à casa que o jogador quer preencher nessa jogada. Ex: se o jogador
quiser preencher a casa do canto inferior direito então a ação é 7.

O programa conta também com a disponibilidade de o utilizador jogar contra o MAX, tirando partindo
do estudo da escolha das ações do adversário, permitindo um estudo da poda alfa-beta. Interessante!!! :)



"""
import copy, random

# ------------------------------------------------------------------
# interface :D
def mostra_tabuleiro(T):
    simbolos = {1: 'X', -1: 'O', 0: '.'}
    print(f"{simbolos[T[0]]} | {simbolos[T[1]]} | -- ")
    print(f"{simbolos[T[2]]} | {simbolos[T[3]]} | {simbolos[T[4]]} ")
    print(f"{simbolos[T[5]]} | {simbolos[T[6]]} | {simbolos[T[7]]} ")

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):
    return[i for i in range(8) if T[i] == 0]

# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jogador):
    # aux fica com cópia do tabuleiro
    aux = copy.copy(T)
    if jogador == 'MAX':
        aux[a] = 1
    elif jogador == 'MIN':
        aux[a] = -1
    return aux

# ------------------------------------------------------------------
# existem 7 possíveis alinhamentos vencedores, para cada jogador
def utilidade(T):
    L_win = {
        (0,2,3), (1,3,4), (2,5,6), (3,6,7), #L normal
        (0,1,2), (2,3,5), (3,4,6), # L invertido sentido esquerda
        (0,1,3), (2,3,6), (3,4,7) # L invertido sentido direita
    }
    for (i,j,k) in L_win:
        if T[i] == T[k] == T[j] != 0:
            return T[i]
    return 0

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):
    return utilidade(T) != 0 or all(x != 0 for x in T)


# ------------------------------------------------------------------
# algoritmo da wikipedia (fail-soft version adaptada)
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T, alfa, beta, jogador):
    if estado_terminal(T):
        return utilidade(T),-1,-1
    if jogador == 'MAX':
        v = -10
        ba=-1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, 'MIN')
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa, v)
            if v >= beta:
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:
        v = 10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T,a,'MIN'), alfa, beta, 'MAX')
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta, v)
            if v <= alfa:
                break
        return v, ba, resultado(T, ba,'MIN')

# ------------------------------------------------------------------
def joga_max(T):
    # passamos o tabuleiro e valores iniciais para alfa e beta
    v, a, e = alfabeta(T, -10, 10, 'MAX')
    print('MAX joga para ', a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
    v, a, e = alfabeta(T, -10, 10, 'MIN')
    print('MIN joga para ', a)
    return e

# -------------------------------------------------------------------

def joga_humano(T):
    aa = acoes(T)
    while True:
        try:
            jogada = int(input(f"Escolha a sua jogada (Digite número de 0 a 7) : "))
            if jogada in aa:
                T[jogada] = -1
                break
            else:
                print("Posição inválida ou já ocupada! ")
        except ValueError:
            print("Entrada inválida! ")
    return T

# ------------------------------------------------------------------
def jogo(p1, p2):
    # cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0]
    # podemos partir de um estado mais "avançado"
    #T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print('Venceu o MAX')
    elif utilidade(T) == -1:
        print('Venceu o MIN')
    else:
        print('Empate')

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    aa = [i for i in range(8) if T[i] == 0]
    if aa:
        x = random.choice(aa)
        T[x] = -1

    return T

# ------------------------------------------------------------------
# main

if __name__ == "__main__":

    #retire comentarios para jogar!

    jogo(joga_max,joga_humano)

    #max vs min
    #jogo(joga_max,joga_min)

    #max vs min aleatorio
    #jogo(joga_max,joga_rand)


