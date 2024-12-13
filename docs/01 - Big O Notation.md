# "BIG O" Notation

_Complexidade Temporal_: Vai dizer quanto tempo demora para executar o algoritmo proporcional ao input - Se a gente percorrer todos os espaços do array: BigO(n)

_Complexidade espacial_: É o quanto de memória a gente precisa para executar o algoritmo

Exemplos:

- `0(1)` - Não importa o tamanho do input. O tempo de execução é sempre o mesmo.

- `O(log n)` - Cresce numa proporção logaritimica.

- `O(n log n)` - Uma parte do algoritmo escala com O(log n) e outra parte com O(n)

  - [Algoritmo de MergeSort para exemplo](https://joaoarthurbm.github.io/eda/posts/merge-sort/)

- `O (n ^ 2) - Quadratic Time` - É como se você fizesse um for loop em cima de outro for loop no mesmo array

- `O(2 ^ n) - Exponetial Time` - Para cada item novo adicionado ao input, o tempo de execução vai demorar o dobro.

- `O(n!) - Factorial Time` - Tempo de execução aumenta fatorialmente ao tamanho do input
