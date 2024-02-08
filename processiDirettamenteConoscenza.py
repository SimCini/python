#PROCESSI DIRETTAMENTE A CONOSCENZA
import os
from multiprocessing import Pipe, Process, current_process

def process_id():
    #Proprietà processo
    print(f"Server PID: {os.getpid()}, Process Name: {current_process().name}, Process PID: {current_process().pid}")

def process_function(conn):
    process_id()
    print("Elaboro il dato ricevuto ed invio il risultato")
    data_received = conn.recv() #riceve il valore della connessione
    result = data_received*2
    conn.send(result) #da il risultato come valore della connessione
    conn.close()

if __name__ == "__main__":
    process_id()
    print("Creo una connessione e un processo figlio")
    parent_conn, child_conn = Pipe() #divide le due connessioni di Pipe() in 2: parent e child
    data = 5
    p = Process(target=process_function, args=(child_conn,))
    p.start()
    parent_conn.send(data) #da il risultato come valore della connessione
    result = parent_conn.recv() #riceve il valore della connessione parent
    p.join() ##blocca il processo principale fino  a quando i processi biforcati hanno finito
    process_id()
    print("Stampo il risultato ricevuto")
    print(result)


