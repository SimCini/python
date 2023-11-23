def datiC(citta):
    x = False
    max = 0
    min = 100
    mesiMax = []
    mesiMin = []
    sommaVal=0
    c=0
    for nC,valori in datiP:
        if nC==citta:
            x=True
            for mese,val in valori:
                if val!="N/D":
                    c+=1
                    sommaVal+=val
                    if val>max:
                        max=val
                    if val<min:
                        min=val
    
    for nC,valori in datiP:
        for mese,val in valori:
            if nC==citta:
                if val==max:
                    mesiMax.append(mese)
                if val==min:
                    mesiMin.append(mese)

    if x:
        if c>0:
            media = sommaVal/c
            return(media,(max,mesiMax),(min,mesiMin))
        else:
            return(None)
    else:
        return("ERRORE: Città non presente, riesegui il programma")

datiP = (
    ("Milano", [("Gennaio", 23),("Febbraio", 24), ("Marzo", 23), ("Aprile", 20), ("Maggio", 18), ("Giugno", 15)]),
    ("Varese", [("Gennaio", 24),("Febbraio", 24), ("Marzo", 23), ("Aprile", "N/D"), ("Maggio", 19), ("Giugno", 16)]),
    ("Como", [("Gennaio", 22),("Febbraio", 24), ("Marzo", 23), ("Aprile", 19), ("Maggio", 17), ("Giugno", "N/D")]),
    ("Ciao", [("Gennaio", "N/D"),("Febbraio", "N/D"), ("Marzo", "N/D"), ("Aprile", "N/D"), ("Maggio", "N/D"), ("Giugno", "N/D")])
)

citta = input("Inserisci città per visualizzare i dati: ")
print("Media(valoreMax,MesiMax),(valoreMin,MesiMin):",datiC(citta))