class Veicolo:
    def __init__(self, codice, marca, modello,prezzo, annoRevisione):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.annoRevisione = annoRevisione

    def scheda_veicolo(self):
        visualizza = ""
        visualizza += f"Codice: {self.codice}\n"
        visualizza += f"Marca: {self.marca}\n"
        visualizza += f"Modello: {self.modello}\n"
        visualizza += f"Prezzo: {self.prezzo}\n"
        visualizza += f"Anno di revisione: {self.annoRevisione}\n"
        return visualizza

    def modifica_scheda(self):
        print(f"Modifica del veicolo")
        scelta = int(input("1. modifica Codice\n2. modifica marca\n3. modifica modello\n4. modifica prezzo\n5. modifica anno di revisione\n0. Uscita\n>>"))

        while (scelta!=0):
            if scelta==1:
                codice = input("Inserisci nuovo codice: ")
                self.codice = codice
            elif scelta==2:
                marca = input("Inserisci nuova marca: ")
                self.marca = marca
            elif scelta==3:
                modello = input("Inserisci nuovo modello: ")
                self.modello = modello
            elif scelta==4:
                prezzo = int(input("Inserisci nuovo prezzo: "))
                self.prezzo = prezzo
            elif scelta==5:
                annoRevisione = int(input("Inserisci anno di revisione aggiornato: "))
                self.annoRevisione = annoRevisione
            else:
                print("Punto del menù non esistente.")
                return
            print("Attributo aggiornato con successo")
            scelta = int(input("1. modifica Codice\n2. modifica marca\n3. modifica modello\n4. modifica prezzo\n5. modifica anno di revisione\n0. Uscita\n>>"))


class Automobile(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,lunghezza,larghezza):
      super().__init__(codice, marca, modello,prezzo, annoRevisione)
      self.lunghezza = lunghezza
      self.larghezza = larghezza

    def scheda_veicolo(self):
        visualizza = ""
        visualizza += f"Codice: {self.codice}\n"
        visualizza += f"Marca: {self.marca}\n"
        visualizza += f"Modello: {self.modello}\n"
        visualizza += f"Prezzo: {self.prezzo}\n"
        visualizza += f"Anno di revisione: {self.annoRevisione}\n"
        visualizza += f"Lunghezza: {self.lunghezza}\n"
        visualizza += f"Larghezza: {self.larghezza}\n"
        return visualizza

class Motociclo(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione, tipo, potenza):
      super().__init__(codice, marca, modello,prezzo, annoRevisione)
      self.tipo = tipo
      self.potenza = potenza

    def scheda_veicolo(self):
        visualizza = ""
        visualizza += f"Codice: {self.codice}\n"
        visualizza += f"Marca: {self.marca}\n"
        visualizza += f"Modello: {self.modello}\n"
        visualizza += f"Prezzo: {self.prezzo}\n"
        visualizza += f"Anno di revisione: {self.annoRevisione}\n"
        visualizza += f"Tipo: {self.tipo}\n"
        visualizza += f"Potenza: {self.potenza}\n"
        return visualizza

class Vendita():
    def __init__(self,codice,data, codiceVenditore):
        self.codice = codice
        self.data = data
        self.codiceVenditore = codiceVenditore
        self.veicoliInVendita = []

    def aggiungi_veicolo(self,veicolo):
        if isinstance(veicolo,Automobile):
            tipo_veicolo ="automobile"

        elif isinstance(veicolo,Motociclo):
            tipo_veicolo ="motociclo"

        if veicolo in self.veicoliInVendita:
            print("Veicolo già in vendita")
        else:
            self.veicoliInVendita.append(veicolo)
            print(f"{tipo_veicolo} aggiunto con successo alla vendita {self.codice} del {self.data}.")

    def rimuovi_veicolo(self,veicolo):
        if isinstance(veicolo,Automobile):
            tipo_veicolo ="automobile"

        elif isinstance(veicolo,Motociclo):
            tipo_veicolo ="motociclo"

        if veicolo in self.veicoliInVendita:
            self.veicoliInVendita.remove(veicolo)
            print(f"{tipo_veicolo} rimosso con successo dalla vendita {self.codice} del {self.data}")
        else:
            print("Veicolo non presente nella vendita")

    def importo_vendita(self):
        importo = 0
        for veicolo in self.veicoliInVendita:
            importo += veicolo.prezzo
        print(f"Importo totale di vendita {self.codice}, contenente {len(self.veicoliInVendita)} veicoli: {importo} €")
    
    def dettaglio_vendita(self):
    #12 Stampa il dettaglio della vendita e restituisce una lista contenente
    # [somma importi automobili, somma importi motocicli, somma importi totali, provvigione ]
    # e il totale della provvigione spettante al venditore sapendo che:
    # per automobili la provvigione spettante è il 3% del prezzo di vendita
    # per motocicli la provvigione spettante è il 2% del prezzo di vendita
      sommaA = 0
      sommaM = 0
      provvigione = 0
      for veicolo in self.veicoliInVendita:
        if isinstance(veicolo,Automobile):
          sommaA += veicolo.prezzo
          provvigione += (veicolo.prezzo*0.03)
        elif isinstance(veicolo,Motociclo):
          sommaM += veicolo.prezzo
          provvigione += (veicolo.prezzo*0.02)

      return([sommaA,sommaM,sommaA+sommaM,provvigione])

class Vendite():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio = nome_negozio
    self.codice_negozio = codice_negozio
    self.listaVendite = []

  def aggiungi_vendita(self,vendita):
    if vendita in self.listaVendite:
      print(f"Vendita {vendita.codice} già presente nella lista")
    else:
      self.listaVendite.append(vendita)
      print(f"Vendita {vendita.codice} aggiunta con successo tra le vendite del negozio {self.nome_negozio}.")

  def rimuovi_vendita(self,vendita):
    if vendita in self.listaVendite:
      self.listaVendite.remove(vendita)
      print(f"Vendita {vendita.codice} rimossa con successo tra le vendite del negozio {self.nome_negozio}.")
    else:
      print(f"Vendita non presente nella lista.")

  def totale_vendite(self):
    totA=0
    totM=0
    tot=0
    for v in self.listaVendite:
      for veicolo in v.veicoliInVendita:
        if isinstance(veicolo,Automobile):
            totA += veicolo.prezzo
        elif isinstance(veicolo,Motociclo):
            totM += veicolo.prezzo

    tot = totA + totM
    return ([totA,totM,tot])


if __name__ == "__main__":

  a1 = Automobile(1,"Audi","Audi Q3",25000,2015,4.5,1.85)
  print(a1.scheda_veicolo())

  a1.modifica_scheda()
  print(a1.scheda_veicolo())

  a2 = Automobile(2,"Peugeot","Peugeot 2008",18000,2014,4.2,1.75)
  m1 = Motociclo(3,"Gilera","Gilera Runner 50",3500,2016,"Scooter",1200)
  m2 = Motociclo(4,"Honda","SW-T 400 – 2013",4500,2012,"Super Sport",1000)

  vendita1=Vendita(1,"01/04/2022",'123')

  vendita1.aggiungi_veicolo(a1)
  vendita1.aggiungi_veicolo(a2)
  vendita1.aggiungi_veicolo(m1)
  vendita1.aggiungi_veicolo(m2)

  vendita1.rimuovi_veicolo(m2)
  vendita1.importo_vendita()

  importi=vendita1.dettaglio_vendita()
  print("--------------------------")
  print(f"\nImporto Automobili= {importi[0]}")
  print(f"\nImporto Motocicli= {importi[1]}")
  print(f"\nImporto Totale= {importi[2]}")
  print(f"\nImporto Provvigione= {importi[3]}")

  print("--------------------------")
  vendite_negozio=Vendite("Concessionaria Magenta ",1)
  vendite_negozio.aggiungi_vendita(vendita1)
  vendite_negozio.rimuovi_vendita(vendita1)
  vendite_negozio.aggiungi_vendita(vendita1)
  importiTotali=vendite_negozio.totale_vendite()
  print("--------------------------")
  print(f"\nImporto totale automobili= {importiTotali[0]}")
  print(f"\nImporto totale motocilci= {importiTotali[1]}")
  print(f"\nImporto totale di tutte le vendite= {importiTotali[2]}")