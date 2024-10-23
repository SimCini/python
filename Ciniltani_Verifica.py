#Verifica effettuata senza uso di risorse

class Articolo:
  def __init__(self, codice, fornitore, marca, prezzo, quantita):
    #1 Implementa il costruttore
    self.codice = codice
    self.fornitore = fornitore
    self.marca = marca
    self.prezzo = prezzo
    self.quantita = quantita

  def scheda_articolo(self):
    #2 Ritorna una stringa contenente gli attributi dell'articolo
    v = ""
    v += f"Codice: {self.codice}\n"
    v += f"Fornitore: {self.fornitore}\n"
    v += f"Marca: {self.marca}\n"
    v += f"Prezzo: {self.prezzo}\n"
    v += f"Quantità: {self.quantita}\n"
    return v

  def modifica_scheda(self):
    #3 Permette di modificare gli attributi dell'articolo
    print(f"Modifica dell'articolo")
    scelta = int(input("1. modifica fornitore\n2. modifica marca\n3. modifica prezzo\n4. modifica quantità\n0. Uscita\n>> "))

    while (scelta!=0):
        if scelta==1:
            fornitore = input("Inserisci nuovo fornitore: ")
            self.fornitore = fornitore
        elif scelta==2:
            marca = input("Inserisci nuova marca: ")
            self.marca = marca
        elif scelta==3:
            prezzo = input("Inserisci nuovo prezzo: ")
            self.prezzo = prezzo
        elif scelta==4:
            quantita = int(input("Inserisci nuovo quantità: "))
            self.quantita = quantita
        else:
            print("Punto del menù non esistente.")
            return
        print("Attributo aggiornato con successo")
        scelta = int(input("1. modifica fornitore\n2. modifica marca\n3. modifica prezzo\n4. modifica quantità\n0. Uscita\n>> "))

class Televisore(Articolo):
  def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
    #4 Implementa il costruttore
    super().__init__(codice,fornitore,marca,prezzo,quantita)
    self.pollici = pollici
    self.tipo = tipo

  def scheda_articolo(self):
    #5 Ritorna una stringa contenente gli attributi del televisore
    v = super().scheda_articolo()
    v += f"Pollici: {self.pollici}\n"
    v += f"Tipo: {self.tipo}\n"
    return v

class Frigorifero(Articolo):
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    #6 Implementa il costruttore
    super().__init__(codice,fornitore,marca,prezzo,quantita)
    self.dimensioni = dimensioni
    self.modello = modello

  def scheda_articolo(self):
    #7 Ritorna una stringa contenente gli attributi del frigorifero
    v = super().scheda_articolo()
    v += f"Dimensioni: {self.dimensioni}\n"
    v += f"Modello: {self.modello}\n"
    return v

class Ordine():
  def __init__(self,codice,data, piva,indirizzo):
    #8 Implementa il costruttore
    self.codice = codice
    self.data = data
    self.piva = piva
    self.indirizzo = indirizzo
    self.ordine = []

  def aggiungi_articolo(self,articolo):
    #9 Completa il metodo aggiungendo l'oggetto alla lista e stampando il messaggio opportuno
    
    
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"

    if articolo in self.ordine:
      print(f"Articolo {tipo_articolo} già presente nell'ordine.")
    else:
      if isinstance(articolo,Televisore) or isinstance(articolo,Frigorifero):
        self.ordine.append(articolo)
        print(f"Articolo {tipo_articolo} aggiunto con successo all'ordine {self.codice}.")
      else:
        self.ordine.append(articolo)
        print(f"Articolo sconosciuto aggiunto con successo all'ordine {self.codice}.")

  def rimuovi_articolo(self,articolo):
    #10 Implementa il metodo
    if isinstance(articolo,Televisore):
      tipo_articolo="televisore"
    elif isinstance(articolo,Frigorifero):
      tipo_articolo="frigorifero"

    if articolo in self.ordine:

      if isinstance(articolo,Televisore) or isinstance(articolo,Frigorifero):
        self.ordine.remove(articolo)
        print(f"Articolo {tipo_articolo} rimosso con successo dall'ordine {self.codice}.")
      else:
        self.ordine.remove(articolo)
        print(f"Articolo sconosciuto rimosso con successo dall'ordine {self.codice}.")
    else:
      print(f"Articolo {tipo_articolo} non presente nell'ordine.")

  def importo_ordine(self):
    #11 Stampa il numero di articoli e per ogni articolo l'importo (prezzo*quantita)

    print(f"Articoli presenti nell'ordine: {len(self.ordine)}")

    for articolo in self.ordine:
      if isinstance(articolo, Televisore):
        tipo_articolo = "televisore"
      elif isinstance(articolo, Frigorifero):
        tipo_articolo = "frigorifero"
      else:
        tipo_articolo = "sconosciuto"  
      print(f"Importo articolo {tipo_articolo} in quantità {articolo.quantita}: {(articolo.prezzo*articolo.quantita):.2f}")

  def dettaglio_ordine(self):
    #12 Stampa i dettagli dell'ordine e restituisce una lista contenente
    # [somma importi televisori, somma importi frigoriferi, somma importi totali ]
    #...

    sommaT = 0
    sommaF = 0

    for articolo in self.ordine:
      if isinstance(articolo, Televisore):
        tipo_articolo = "televisore"
        sommaT += articolo.prezzo*articolo.quantita
      elif isinstance(articolo, Frigorifero):
        tipo_articolo = "frigorifero"
        sommaF += articolo.prezzo*articolo.quantita

      v = f"\nArticolo: {tipo_articolo}\n"
      if isinstance(articolo, Televisore):
        v += f"Importo: {sommaT}"
      elif isinstance(articolo, Frigorifero):
        v += f"Importo: {sommaF}" 

      print(v+"\n")
      print(articolo.scheda_articolo())

    return([sommaT,sommaF,sommaT+sommaF]) #è errato ritornare sommaT e sommaF con self (es. self.sommaT) --> non sono attributi
  
class Ordini():

  def __init__(self,nome_negozio,codice_negozio):
    #16 Implementa il costruttore
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.ordini = []

  def aggiungi_ordine(self,ordine):
    #17 Implementa il metodo
    if ordine in self.ordini:
      print(f"Ordine {ordine.codice} già presente nella lista ordini.")
    else:
      self.ordini.append(ordine)
      print(f"Ordine {ordine.codice} aggiunto con successo alla lista di ordini.")

  def rimuovi_ordine(self,ordine):
    #18 Implementa il metodo
    if ordine in self.ordini:
      self.ordini.remove(ordine)
      print(f"Ordine {ordine.codice} rimosso con successo dalla lista di ordini.")
    else:
      print(f"Ordine {ordine.codice} non presente nella lista ordini.")

  def totale_ordini(self):
    #19 Implementa il metodo
    #...
    totT = 0
    totF = 0
    tot = 0 #facoltativo perchè si potrebbe fare totT + totF

    for ordine in self.ordini:
      print(f"\n- ORDINE {ordine.codice}")
      importi = ordine.dettaglio_ordine()
      totT += importi[0]
      totF += importi[1]
      tot += importi[2] #facoltativo perchè si potrebbe fare totT + totF

    return ([totT, totF, tot])
  

if __name__ == "__main__":

  t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
  print(t1.scheda_articolo())
  t1.modifica_scheda()
  print(t1.scheda_articolo())

  #Blocco 1 finito alle 9:44

  t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
  f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
  f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

  ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
  ordine1.aggiungi_articolo(t1)
  ordine1.aggiungi_articolo(t2)
  ordine1.aggiungi_articolo(f1)
  ordine1.aggiungi_articolo(f2)

  ordine1.rimuovi_articolo(f2)
  ordine1.rimuovi_articolo(f2)

  ordine1.importo_ordine()

  importi = ordine1.dettaglio_ordine()
  print("--------------------------")
  print(f"\nImporto televisori= {importi[0]}")
  print(f"\nImporto frigoriferi= {importi[1]}")
  print(f"\nImporto totale= {importi[2]}\n")

  #Blocco 2 (classe Ordine) finita alle 10.12

  ordini_negozio=Ordini("Megastore vendita ",1)
  ordini_negozio.aggiungi_ordine(ordine1)
  ordini_negozio.rimuovi_ordine(ordine1)
  ordini_negozio.rimuovi_ordine(ordine1)
  ordini_negozio.aggiungi_ordine(ordine1)

  t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
  f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
  ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
  ordine2.aggiungi_articolo(t3)
  ordine2.aggiungi_articolo(f3)

  ordini_negozio.aggiungi_ordine(ordine2)

  importiTotali=ordini_negozio.totale_ordini()
  print("--------------------------")
  print(f"\nImporto totale televisori= {importiTotali[0]}")
  print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
  print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

  #Blocco 3 (Ordini) finito alle 10.50