#PROCESSI INDIRETTAMENTE A CONOSCENZA
from multiprocessing import Queue, Process, current_process
import os #permette di interagire con il sistema operativo
"""
Queue --> Classe che rappresenta una coda condivisa tra processi
è utilizzata per consentire la comunicazione tra processi, consentendo
loro di scambiarsi dati in modo sicuro.
"""

def process_id():
    #Stampa le proprietà del processo
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(data, result_queue):
    process_id()
    print("Elabora: ",data) #indica che dato sta elaborando
    result = data*2 
    result_queue.put(result) #mette in coda il risultato ottenuto

if __name__=="__main__":
    data_list = [1,2,3,4]
    result_queue = Queue() #Inizializzazione della coda
    processes = []

    for data in data_list:
        p = Process(target=process_function, args=(data, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Il main stampa i risultati")
    while not result_queue.empty(): #Mentre la coda non è vuota stampa i risultati e mano mano li toglie dalla coda
        result = result_queue.get()
        print(result)