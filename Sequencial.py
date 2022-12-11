import queue
from random import randint
import time

fila = queue.Queue()
valor_maximo_fila = 100
tempo_lista = []
    
#Função para criar a fila
def criar_fila(): 
    for i in range(10): 
        fila.put(randint(0, valor_maximo_fila)) 
    print(f"Fila inicialmente --> {fila.queue}\n")

#Função com a operação de retirada e adição
def update_fila(qtd_threads):
    tempo_inicio = time.time()
    
    velho = fila.get()
    novo = randint(0, valor_maximo_fila)
    fila.put(novo)
    print(f"Thread {qtd_threads},  tira {velho},  poe {novo},  fila: {fila.queue}")

    tempo_fim = time.time()
    tempo_lista.append((tempo_fim - tempo_inicio))

#execução da operação sequencial
def sequencial():

    qtd_threads = 0
    criar_fila()
    
    while(sum(tempo_lista) < 1):
        update_fila(qtd_threads)
        qtd_threads = qtd_threads + 1 
    
    duracao = sum(tempo_lista)
    inser_por_seg = qtd_threads / duracao
    return [duracao, inser_por_seg]
