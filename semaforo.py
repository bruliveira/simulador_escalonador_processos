#SÓ TEM AS FUNÇÕES DE FILAS 
import threading
import time
from random import randint

valor_maximo_fila = 100
tamanho_fila = 10
fila = []

semaforo = threading.Semaphore(2)


def criar_fila(): #Criando a fila com as 10 posições iniciais
    x = 0
    while x < tamanho_fila:
        fila.append(randint(0, valor_maximo_fila))
        x += 1
    print(f"Fila inicialmente --> {fila}")

def exibir_fila(velho, novo, fila):
    print(f"Thread ---,  tira {velho},  poe {novo},  fila: {fila}")

def operacao():
    velho = fila.pop(0) #Retirando o primeiro elemento da fila...
    novo = randint(0, valor_maximo_fila)
    fila.append(novo) #Adiconando elemento no final da fila...
        
    print("Número retirado: ", velho)
    print("Número adicionado: ", novo)
    
    exibir_fila(velho, novo, fila)
    
    #print(fila)    
        
def mostrar():
    semaforo.acquire()
    print(threading.currentThread().getName())
    time.sleep(randint(2,7))
    semaforo.release()
    
if __name__=="__main__":
    t1 = threading.Thread(target=mostrar)
    t2 = threading.Thread(target=mostrar)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    criar_fila()
    print("Depois da --> OPERAÇÂO")
    operacao()
   
    

    
