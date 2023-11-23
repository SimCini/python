def media_globale(tupla):
    sommaVal=0
    c=0
    '''
    for locazione,dati in tupla:
        for anno,mesi in dati:
            if anno==2023:
                for mese,valore in mesi:
                    if valore!="N/D":
                        sommaVal+=valore
                        c+=1
    
    '''
    for t in tupla:
        (citta,prov),(anno,(mese,val)) = t
        if anno==2023 and val!="N/D":
            sommaVal+=val
            c+=1
    media = sommaVal/c
    return(media)

def media(tupla, prov, mes):
    somma=0
    c=0
    '''
    for locazione,dati in tupla:
        for citta,provincia in locazione:
            if provincia==prov:
                for anno,mesi in dati:
                    for mes,valore in mesi:
                        if mes==mese:
                            somma+=valore
                            c+=1
    '''
    for t in tupla:
        (citta,provincia),(anno,(mese,val)) = t
        if provincia==prov and mese==mes and val!="N/D":
            somma+=val
            c+=1
    if c>0:                        
        media = somma/c
        return(media)
    else:
        return None

def pioggiaMax(tupla):
    max=0
    cittaMax = []
    mesiMax = []
    for locazione,dati in tupla:
        for citta,provincia in locazione:
            if provincia=="Milano":
                for anno,mesi in dati:
                    for mese,valore in mesi:
                        if valore>max:
                            max = valore
    for locazione,dati in tupla:
        for citta,provincia in locazione:
            if provincia=="Milano":
                for anno,mesi in dati:
                    for mese,valore in mesi:
                        if valore==max:
                            cittaMax.append(citta)
                            mesiMax.append(mese)
    return(cittaMax,mesiMax)

def pioggiaMin(tupla):
    min=100
    mesiMin = []
    for locazione,dati in tupla:
        for anno,mesi in dati:
            for mese,valore in mesi:
                if valore<min:
                    min = valore
    for locazione,dati in tupla:
        for anno,mesi in dati:
            for mese,valore in mesi:
                if valore==min:
                    mesiMin.append(mese)
    return(mesiMin)

def provinciaPer(tupla):
    tot=0
    t = ()
    for locazione,dati in tupla:
        for anno,mesi in dati:
            for mese,valore in mesi:
                tot+=valore
    
    for locazione,dati in tupla:
        for citta,prov in locazione:
            for anno,mesi in dati:
                for mese,valore in mesi:
                    for p in prov:
                        perc = valore*100/tot
                        t.__add__ = (p, perc)
    return t

    
    


tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),
                      (("Vittuone","Milano"),(2023, ("maggio",80))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),
                      (("Vittuone","Milano"),(2023, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2023, ("luglio",165)))
                      )

print("Media globale dell'anno 2023: ",media_globale(tupla_pluviometrica))

print("-MEDIA DI PROVINCIA E MESE-")
provincia = input("Inserisci provincia:")
mese = input("Inserisci mese: ")
print(f"Media della provincia {provincia} nel mese di {mese}: ",media(tupla_pluviometrica,provincia,mese))

print("Città e mese/i più piovosa/e della provincia di Milano (città, mesi): ",pioggiaMax)