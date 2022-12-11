import queue
import threading
from random import randint
import time

fila = queue.Queue()
valor_maximo_fila = 100
tempo_lista = []

semaphore = threading.Semaphore(2) # Quantidade - semáforos
    
#Função para criar a fila
def criar_fila(): 
    for i in range(10): 
        fila.put(randint(0, valor_maximo_fila)) 
    print(f"Fila inicialmente --> {fila.queue}\n")

#Função com semaforo
def update_fila(qtd_threads):
    tempo_inicio = time.time()
    
    semaphore.acquire()
    
    velho = fila.get()
    novo = randint(0, valor_maximo_fila)
    fila.put(novo)
    
    print(f"Thread {qtd_threads},  tira {velho},  poe {novo},  fila: {fila.queue}")

    semaphore.release()
    
    tempo_fim = time.time()
    tempo_lista.append((tempo_fim - tempo_inicio))

#Execução da função com semaforo
def concorrente():

    qtd_threads = 0
    th = []
    criar_fila()
    
    while(sum(tempo_lista) < 1):
        th.append(threading.Thread(target=update_fila, args= (qtd_threads,)))
        th[qtd_threads].start()
        th[qtd_threads].join()
        qtd_threads = qtd_threads + 1
        
    duracao = sum(tempo_lista)
    inser_por_seg = qtd_threads / duracao 
    """print("Tempo total: ", duracao)  
    print("\nSem semaforo: Número de inserções por segundos: ", inser_por_seg)"""

    return [duracao, inser_por_seg]