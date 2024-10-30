# tic-tac-toe-alphabetapruning


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
