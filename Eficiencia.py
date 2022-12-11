import semaforo
import Sequencial

if __name__=="__main__":

    sem_semaforo = Sequencial.sequencial()
    com_semaforo = semaforo.concorrente()

    print("\n\n------------- CONCORRENTE ----------------")
    print("Duração (seg): ", com_semaforo[0])
    print("Inserção por segundo: ", com_semaforo[1])

    print("\n\n-------------- SEQUENCIAL ----------------")
    print("Duração (seg): ", sem_semaforo[0])
    print("Inserção por segundo: ", sem_semaforo[1])
    print("------------------------------------------\n")

    """eficiencia = sem_semaforo[1] - com_semaforo[1]

    if eficiencia > 0:
        resuk = sem_semaforo[1]/com_semaforo[1]
        print("O modelo sequencial é {0:.3f} mais eficiente que o concorrente.\n".format(sem_semaforo_per_com_semaforo))
    else:
        com_semaforo_per_sem_semaforo = com_semaforo[1]/sem_semaforo[1]
        print("O modelo concorrente é {0:.3f} mais eficiente que o sequencial.\n".format(com_semaforo_per_sem_semaforo))"""