def prezzo_medioP(prezzi_prodotti, prodotto, giorno):
    c=0
    sommaPrezzi=0
    for prodotti,*prezzi in prezzi_prodotti:
        for giorni,prezzo in prezzi:
            if (giorni==giorno and prodotti==prodotto):
                c+=1
                sommaPrezzi+=prezzo
    if c>0:
        media = sommaPrezzi/c
        return media
    else:
        return("Prodotto inesistente")
    
def prezzoMedioAll(prezzi_prodotti):
    sommaPrezzi=0
    for prodotti,*prezzi in prezzi_prodotti:
        for giorno, prezzo in prezzi:
            sommaPrezzi+=prezzo
    media=sommaPrezzi/len(prezzi)
    return media

def prezzoMaxP(prezzi_prodotti,prodMax):
    max = 0
    giorniMax=[]
    for prodotti,*prezzi in prezzi_prodotti:
        for giorno, prezzo in prezzi:
            if(prodotti==prodMax and prezzo>max):
                max = prezzo
    for prodotti,*prezzi in prezzi_prodotti:
        for giorno, prezzo in prezzi:
            if(prodotti==prodMax and max==prezzo):
                giorniMax.append(giorno)
                
    return(max," --> nei giorni: ",giorniMax)

def prezzoMin(prezzi_prodotti):
    min = 100
    giorniMin=[]
    prodottiMin=[]
    for prodotti,*prezzi in prezzi_prodotti:
        for giorno, prezzo in prezzi:
            if(prezzo<min):
                min = prezzo
    for prodotti,*prezzi in prezzi_prodotti:
        for giorno, prezzo in prezzi:
            if(min==prezzo):
                giorniMin.append(prodotti+" Nei giorni:"+giorno)
            
    return(min, giorniMin)
    


prezzi_prodotti = (
    ("Mela", ("Lunedì", 1.0), ("Martedì", 1.2), ("Mercoledì", 1.1), ("Giovedì", 1.0), ("Venerdì", 1.2), ("Sabato", 1.3)),
    ("Banana", ("Lunedì", 1.1), ("Martedì", 1.2), ("Mercoledì", 1.4), ("Giovedì", 1.0), ("Venerdì", 1.3), ("Sabato", 1.4)),
)

nomeProd = input("Inserisci prodotto da controllare: ")
giorno = input("Inserisci giorno della settimana: ")
print(f"Il prezzo medio del prodotto {nomeProd} è: ",prezzo_medioP(prezzi_prodotti, nomeProd, giorno))

print("Il prezzo medio di tutti i prodotti è: ",prezzoMedioAll(prezzi_prodotti))

prodMax = input("Inserisci prodotto per controllare il massimo: ")
print(f"Prezzo max di{prodMax} è:",prezzoMaxP(prezzi_prodotti,prodMax))

print(f"Prezzo min di tutti i prodotti è:",prezzoMin(prezzi_prodotti))