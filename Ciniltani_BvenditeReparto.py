def mediaReparto(nome):
    x = False
    sommaVal=0
    c=0
    max=0
    min=100
    mesiMax = []
    mesiMin = []
    for reparto,dati in venditeMens:
        if reparto==nome:
            x = True
            for mese,valore in dati:
                if valore!="N/D":
                    sommaVal+=valore
                    c+=1
                    if valore>max:
                        max=valore
                    if valore<min:
                        min=valore
    
    for reparto,dati in venditeMens:
        if reparto==nome:
            for mese,valore in dati:
                if valore==max:
                    mesiMax.append(mese)
                if valore==min:
                    mesiMin.append(mese)
    if x:
        if c>0:
            media = sommaVal/c
            return(media,(max,mesiMax),(min,mesiMin))
        else:
            return(None)
    else:
        return("Errore: città inserita non presente")



venditeMens = (
    ("reparto1", [("Gennaio", 23),("Febbraio", 24), ("Marzo", 23), ("Aprile", 20), ("Maggio", 18), ("Giugno", 15)]),
    ("reparto2", [("Gennaio", 24),("Febbraio", 24), ("Marzo", 23), ("Aprile", "N/D"), ("Maggio", 19), ("Giugno", 16)]),
    ("reparto3", [("Gennaio", 22),("Febbraio", 24), ("Marzo", 23), ("Aprile", 19), ("Maggio", 17), ("Giugno", "N/D")]),
    ("reparto4", [("Gennaio", "N/D"),("Febbraio", "N/D"), ("Marzo", "N/D"), ("Aprile", "N/D"), ("Maggio", "N/D"), ("Giugno", "N/D")])
)

reparto = input("Inserisci reparto per visualizzare i dati Media, Max e Min: ")
print("(Media importo, (ValoreMax,MesiMax), (ValoreMin,MesiMin)): ",mediaReparto(reparto))

