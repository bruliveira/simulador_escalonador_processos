#Funções para fila ----> Ok
#Thread --> ok(duas) - Ver se precisa colocar um for para a função rodar varias vezes, ou algo assim
#Semaforo

#Depois adicionar os extras...(:

import threading
import time
from random import randint

valor_maximo_fila = 100
tamanho_fila = 10
fila = []

semaforo = threading.Semaphore(2) #Definindo a quantidade de Threads

def criar_fila(): #Criando a fila com as 10 posições iniciais
    x = 0
    while x < tamanho_fila:
        fila.append(randint(0, valor_maximo_fila))
        x += 1
    print(f"Fila inicialmente --> {fila}\n")

def exibir_fila(velho, novo, fila):
    print(f"Thread ---,  tira {velho},  poe {novo},  fila: {fila}")

'''SEM THREAD
def operacao():
    velho = fila.pop(0) #Retirando o primeiro elemento da fila...
    novo = randint(0, valor_maximo_fila)
    fila.append(novo) #Adiconando elemento no final da fila...
        
    print("Número retirado: ", velho)
    print("Número adicionado: ", novo)
    
    exibir_fila(velho, novo, fila)
    
'''

def operacao():
    time.sleep(randint(0,10))
    
    velho = fila.pop(0) #Retirando o primeiro elemento da fila...
    novo = randint(0, valor_maximo_fila)
    fila.append(novo) #Adiconando elemento no final da fila...

    print(f"Thread {threading.currentThread().getName()},  tira {velho},  poe {novo},  fila: {fila}") 
    
    '''
    - são algumas coisas durante o teste, deixar aqui, caso precise
    print("Número retirado: ", velho)
    print("Número adicionado: ", novo)
    print('Iniciou: ' + threading.currentThread().getName())
    print('Terminou: ' + threading.currentThread().getName())
    
    #exibir_fila(velho, novo, fila)
    
def mostrar():
    semaforo.acquire()
    print(threading.currentThread().getName())
    time.sleep(randint(2,7))
    semaforo.release()
    '''
if __name__=="__main__":
    print(f"\n--> Criando a fila com, as 10 posições <--")
    criar_fila()
    
    #Threads
    thread1 = threading.Thread(target=operacao, name = 'T1')
    thread2 = threading.Thread(target=operacao, name = 'T2')
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
