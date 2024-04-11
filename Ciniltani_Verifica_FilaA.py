def infoTupla(targa,mese):
  controlloMese = False
  controlloTarga = False
  if targa in noleggi.keys():
    controlloTarga=True
    for i in noleggi[targa]:
      mesi,noleggiSett,km = i
      if mesi==mese:
        controlloMese=True
        print(f"Tupla di {mese}, targa: {targa}")
        print(i)
        return
    print("Mese non presente.")
  else:
    print("Errore, targa non trovata")

def info(targa,mese):
  controlloMese = False
  controlloTarga = False
  if targa in noleggi.keys():
    controlloTarga=True
    for mesi,noleggiSett,km in noleggi[targa]:
      if mesi==mese:
        controlloMese=True
        print(f"Informazioni di {mese}, targa: {targa}")
        print(f"numero noleggi settimanali:{noleggiSett}\nKm effettuati: {km}")
        return
    print("Mese non presente.")
  else:
    print("Errore, targa non trovata")

def infoNoleggi(targa,mese):
  controlloMese = False
  controlloTarga = False
  if targa in noleggi.keys():
    controlloMese=True
    for mesi,noleggiSett,km in noleggi[targa]:
      if mesi==mese:
        controlloMese=True
        print(f"Numero noleggi settimanali di {mese} per targa {targa}")
        print(f"1a settimana: {noleggiSett[0]}\n2a settimana: {noleggiSett[1]}\n3a settimana: {noleggiSett[2]}\n4a settimana: {noleggiSett[3]}")
        return
    print("Mese non presente.")
  else:
    print("Errore, targa non trovata")
def maxNoleggi(mese):
  max=0
  targaMax = ""
  controlloMese = False
  for chiave,valori in noleggi.items():
    for mesi,noleggiSett,km in valori:
      if mesi==mese:
        controlloMese=True
        for nSett in noleggiSett:
          if nSett>max:
            max=nSett
            targaMax=chiave

  if max==0 or targaMax=="" or not(controlloMese):
    return ("Errore, dati non trovati")
  else:
    print(f"Numero massimi di noleggi settimanali in {mese}: {max} --> effettuati da {targaMax}")
    return

def kmTot():
  kmTotali = 0
  for chiave,valori in noleggi.items():
    for mesi,noleggiSett,km in valori:
        kmTotali+=km
  print(f"Somma di tutti i km (tutti i mesi e tutti i veicoli): {kmTotali}")
  return

def meseKmMaggiori(targa):
  maxKm=0
  meseMax = ""
  controlloTarga = False
  if targa in noleggi.keys():
    controlloTarga=True
    for mese,noleggiSett,km in noleggi[targa]:
      if km>maxKm:
        maxKm=km
        meseMax=mese
  if maxKm==0 or meseMax=="" or not(controlloTarga):
    return ("Errore, dati non trovati")
  else:
    print(f"Maggior numero di km fatti da {targa} sono: {maxKm}, nel mese di {meseMax}")
    return

#Funzioni per inserimento di una nuova macchina
def aggiungi(targa):
  mesi = ["Giugno","Luglio","Agosto","Settembre"]
  for mese in mesi:
    print(f"-Dati di {mese}-")
    sett1 = int(input("Inserisci n noleggi prima settimana: "))
    while (sett1<0):
      sett1 = int(input("Inserisci n noleggi prima settimana: "))
    sett2 = int(input("Inserisci n noleggi seconda settimana: "))
    while (sett2<0):
      sett2 = int(input("Inserisci n noleggi seconda settimana: "))
    sett3 = int(input("Inserisci n noleggi terza settimana: "))
    while (sett3<0):
      sett3 = int(input("Inserisci n noleggi terza settimana: "))
    sett4 = int(input("Inserisci n noleggi quarta settimana: "))
    while (sett4<0):
      sett4 = int(input("Inserisci n noleggi quarta settimana: "))
    noleggiSettimanali = (sett1,sett2,sett3,sett4)

    km = int(input(f"Inserisci km effettuati nel mese di {mese}: "))
    while (km<0):
      km = int(input(f"Inserisci km effettuati nel mese di {mese}: "))
    
    info = (mese,noleggiSettimanali,km)

    if targa in noleggi.keys():
      noleggi[targa].append(info)
    else:
      noleggi[targa]=[info]

  print("Macchina inserita con successo: ",noleggi[targa])

  
################################################################################
#PUNTO 1
noleggi = {
    "AA123BB": [("Giugno",(9,4,5,7),1293),
                ("Luglio",(14,3,5,12),3231),
                ("Agosto",(19,14,15,17),4020),
                ("Settembre",(6,8,5,7),3928),
                ],
    "AB345CD": [("Giugno",(20,24,15,7),1391),
                ("Luglio",(9,14,5,17),1234),
                ("Agosto",(20,24,15,17),4932),
                ("Settembre",(10,14,5,7),2872),
                ],
    "CD456FF": [("Giugno",(10,14,5,7),2872),
                ("Luglio",(19,4,15,7),3273),
                ("Agosto",(20,14,6,6),3211),
                ("Settembre",(10,14,5,7),2827),
                ],
}
#PUNTO 2
noleggi["ZZ999CS"] = [("Giugno",(10,10,10,10),1000*3),
                      ("Luglio",(10,10,10,10),1000*3),
                      ("Agosto",(10,10,10,10),1000*3),
                      ("Settembre",(10,10,10,10),1000*3),
                      ]
#Controllato 09:25

#PUNTO 3
noleggi["AA123BB"].append(("Ottobre",(19,11,10,9),2380))
noleggi["AB345CD"].append(("Ottobre",(12,10,11,17),2980))
noleggi["CD456FF"].append(("Ottobre",(14,12,10,17),2650))
noleggi["ZZ999CS"].append(("Ottobre",(17,14,12,18),3150))
#Controllato 09:29

#PUNTO 4
infoTupla("AA123BB","Settembre")
print()
#Controllo 9:41

#PUNTO 5
info("CD456FF","Luglio")
print()
#Controllato 9:47

#PUNTO 6
infoNoleggi("AA123BB","Luglio")
print()
#Controllato 9:52

#PUNTO 7
maxNoleggi("Luglio")
print()
#Controllato 10:02

#PUNTO 8
kmTot()
print()
#Controllato 10:08

#PUNTO 9
meseKmMaggiori("CD456FF")
print()
#Controllato 10:15

#PUNTO 10
#Inserimento di una nuova macchina
print("-Inserimento di una nuova macchina-")
targa = input("Inserisci targa: ")
while (len(targa)!=7 or (targa in noleggi.keys())):
  targa = input("Reinserisci targa: ")
aggiungi(targa)
#Controllato 10:37

#Visualizza tutto il dizionario (non richiesto)
'''
for i in noleggi.items():
  print(i)
'''
