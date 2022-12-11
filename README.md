<h1 align="center">
📄<br>READ ME
</h1>

## CC0026 - Sistemas Operacionais: Semáforos

# Projeto Final

Este projeto visa expor os problemas advindos do acesso concorrente de tarefas a estruturas de dados compartilhadas e compreender a coordenação dos acessos através de semáforos.
 
# Problema
 
Você deve criar um programa com duas threads, que manipulam uma fila de inteiros de forma concorrente. Cada thread retira o primeiro elemento da fila e coloca um novo elemento no fim da fila:
 
 ```
while (1) {
  velho = retira_primeiro_elemento_da_fila()
  novo = random() % 100
  poe_elemento_no_fim_da_fila (novo)
  imprime operação efetuada e estado da fila
}
```
 
Como fila, deve ser usada a implementação de fila circular construída anteriormente.
 
# Observações
 
A saída do programa deve seguir o formato abaixo (obviamente com valores aleatórios):

```
thread 1: tira 34, põe 81, fila: 47  2 19 66 32 60  9 11 38 81
thread 4: tira 47, põe 55, fila:  2 19 66 32 60  9 11 38 81 55
thread 2: tira  2, põe 31, fila: 19 66 32 60  9 11 38 81 55 31
thread 3: tira 19, põe 17, fila: 66 32 60  9 11 38 81 55 31 17
…
```

A fila tem capacidade para 10 inteiros, está inicialmente cheia (valores aleatórios) e tem comportamento FIFO.

# Roteiro

* Implemente o programa usando semáforos e observe se a fila se comporta corretamente.
* Proponha e implemente uma forma de medir o número de inserções de inteiros na fila por segundo.
* Meça o desempenho de sua solução.

# A entregar

1. A implementação solicitada (código fonte)
2. Uma apresentação do google apresentações, descrevendo os resultados observados nas experiências.

# Colaboradores

Bruna Flávia Alves Oliveira, Maria Adriana da Silva.
