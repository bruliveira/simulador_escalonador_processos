import semaforo
import Sequencial

if __name__=="__main__":

    sem_semaforo = Sequencial.sequencial()
    com_semaforo = semaforo.concorrente()

    print("\n\n------------- CONCORRENTE ----------------")
    print("Duração (seg): ", com_semaforo[0])
    print("Inserção por segundo: ", int(com_semaforo[1]))

    print("\n-------------- SEQUENCIAL ----------------")
    print("Duração (seg): ", sem_semaforo[0])
    print("Inserção por segundo: ", int(sem_semaforo[1]))
    print("------------------------------------------\n")

    if sem_semaforo[1] >= com_semaforo[1] : #caso tenha mais inserção no sequencial do que o concorrente
        eficiencia = (sem_semaforo[1] - com_semaforo[1] /com_semaforo[1])*100 #variação percentual entre os valores
        print("O modelo sequencial é {0:.2f}% mais eficiente que o concorrente.\n".format(eficiencia))
    else: #caso contrário
        eficiencia = ((com_semaforo[1] - sem_semaforo[1]) / sem_semaforo[1])*100
        print("O modelo concorrente é {0:.2f}% mais eficiente que o sequencial.\n".format(eficiencia))