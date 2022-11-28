import threading
import time
from random import randint

valor_maximo_fila = 100
quatidade_teste = 1
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

def operacao():
    #x = 0
    #while x < quatidade_teste:
     
    print('Iniciou: ' + threading.currentThread().getName())
    time.sleep(randint(0,10))
    velho = fila.pop(0) #Retirando o primeiro elemento da fila...
    novo = randint(0, valor_maximo_fila)
    fila.append(novo) #Adiconando elemento no final da fila...
    print('Terminou: ' + threading.currentThread().getName())
    #print(f"-> Thread {threading.currentThread().getName()},\ttira {velho},\tpoe {novo},\t\tfila: {fila}")
    print(f"Thread {threading.currentThread().getName()}, tira {velho}, poe {novo}, fila: {fila}")
        
        #x += 1                               
          
    
def atendimento(id):
    semaforo.acquire()
    print("Thread {}".format(id) + " em andamento")
    x = 0
    while x < quatidade_teste:
        velho = fila.pop(0) #Retirando o primeiro elemento da fila...
        novo = randint(0, valor_maximo_fila)
        fila.append(novo) #Adiconando elemento no final da fila...
        #print(f"-> Thread {threading.currentThread().getName()},\ttira {velho},\tpoe {novo},\t\tfila: {fila}")
        time.sleep(randint(3,10))
        print(f"Thread {id}, tira {velho}, poe {novo}, fila: {fila}")
        
        x += 1    
    
    print("Finalizando...{}".format(id))
    
    semaforo.release()
    
if __name__=="__main__":
    print(f"\n--> Criando a fila com, as 10 posições <--")
    criar_fila()
    
    threadsaqui =  []
    for i in range(1, 5):
    #Threads
        theread = threading.Thread(target= atendimento, args=(i, ))
        threadsaqui.append(theread)
    for thread in threadsaqui:
        thread.start()

    for thread in threadsaqui:
        thread.join()
    
    
