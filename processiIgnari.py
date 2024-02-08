#PROCESSI TOTALMENTE IGNARI
from multiprocessing import Process

"""
multiprocessing è una libreria per gestire la creazione, comunicazione e la sincronizzazione
tra processi nella programmazione parallela e concorrente
Process è una classe per creare processi eseguendo una funzione specificata come target.
"""

def process_function(data): #Permette di moltiplicare i dati del processo * 2, e visualizza i risultati
    result = data*2
    print(result)

if __name__ == "__main__":
    data_list = [1,2,3,4] 
    processes = [] #lista di processi

    for data in data_list:
        p = Process(target=process_function, args=(data,))
        processes.append(p)
        p.start() #avvia l'esecuzione del processo separato
        #--> in questo caso inizia il processo per il processo separato p, e viene chiamato il metodo process_function()

    for p in processes:
        p.join() #blocca il processo principale fino  a quando il processo separato (biforcato) non termina

    