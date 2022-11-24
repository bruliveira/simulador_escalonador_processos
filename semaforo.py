#SÓ TEM AS FUNÇÕES DE FILAS 
import threading
import time
from random import randint

semaforo = threading.Semaphore(2)

fila = []
    
def criar_fila(): #Criando a fila com as 10 posições iniciais
    valor_maximo_fila = 100
    tamanho_fila = 10
    x = 0
    while x < tamanho_fila:
        fila.append(randint(0, valor_maximo_fila))
        x += 1
    print(fila)
    
def retira_primeiro_elemento_da_fila(): #Retirando o primeiro elemento da fila...
    fila.pop(0)
    print(fila)

def poe_elemento_no_fim_da_fila(): #Adiconando elemento no final da fila...
    valor_maximo_fila = 100
    fila.append(randint(0, valor_maximo_fila))
    print(fila)
    
def operacao():
    #while (i):
    velho = retira_primeiro_elemento_da_fila() #O que foi retirado
    novo = poe_elemento_no_fim_da_fila()
    retira_primeiro_elemento_da_fila()
    poe_elemento_no_fim_da_fila()
    print(fila)    
        
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
    retira_primeiro_elemento_da_fila()
    poe_elemento_no_fim_da_fila()
    print("OPERAÇÂO")
    operacao()
    
