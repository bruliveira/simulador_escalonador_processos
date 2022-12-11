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

#Função com a operação de retirada e adição
def operacao(quantidade_thread):
    tempo_inicio = time.time()
    
    velho = fila.get()
    novo = randint(0, valor_maximo_fila)
    fila.put(novo)
    print(f"Thread {quantidade_thread},  tira {velho},  poe {novo},  fila: {fila.queue}")

    tempo_fim = time.time()
    tempo_lista.append((tempo_fim - tempo_inicio))

#execução da operação sequencial
def sequencial_executar():
    quantidade_thread = 1
    
    while(sum(tempo_lista) < 1):
        operacao(quantidade_thread)
        quantidade_thread = quantidade_thread + 1
        
    print("Tempo total: ", sum(tempo_lista))   
  
    inser_segundos = quantidade_thread
    print("\nSem semaforo: Número de inserções por segundos: ", inser_segundos)

#Função com semaforo
def sema(quantidade_thread):
    tempo_inicio = time.time()
    semaphore.acquire()
    
    velho = fila.get()
    novo = randint(0, valor_maximo_fila)
    fila.put(novo)
    
    print(f"Thread {quantidade_thread},  tira {velho},  poe {novo},  fila: {fila.queue}")

    semaphore.release()
    tempo_fim = time.time()
    tempo_lista.append((tempo_fim - tempo_inicio))

#Execução da função com semaforo
def semaforo_executar():
    quantidade_thread = 0
    th = []
    sema(quantidade_thread)
    
    while(sum(tempo_lista) < 1):
        th.append(threading.Thread(target=sema, args= (quantidade_thread,)))
        th[quantidade_thread].start()
        th[quantidade_thread].join()
        quantidade_thread = quantidade_thread + 1
    
    print("Semáforo - Tempo total: ", sum(tempo_lista))     
    inser_segundos = quantidade_thread
    print("\nCom semaforo: Número de inserções por segundos: ", inser_segundos)
    
if __name__=="__main__":
    print(f"\n--> Criando a fila com, as 10 posições <--")
    criar_fila()
    
    #semaforo_executar()
    sequencial_executar()
    
