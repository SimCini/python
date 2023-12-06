def media_globale(tVendite):
    sommaImp=0
    c=0
    '''
    for vendite in tVendite:
        #(reparto,tipo),(prodotto,(pagamento,importo))=vendite
        # print(datiProdotto)
        # print(datiProdotto[0])
        # print(datiProdotto[1][0])
        
        for nome,paga in datiProdotto: #ERRORE incomprensibile di Python
            for tipo,importo in paga:
                sommaImp+=importo
                c+=1
    '''
    for reparto,(prodotto,(tipPagamento,importo)) in tVendite:
        sommaImp+=importo
        c+=1  
    media = sommaImp/c
    return(media)

def media(tVendite, cat, tPagamento):
    sommaV=0
    c=0
    '''
    for reparto,prodotto in tVendite:
        for rep,categoria in reparto:
            if categoria==cat:
                for prod,pagamento in prodotto:
                    for tipPagamento,importo in pagamento:
                        if tipPagamento==tPagamento:
                            sommaV+=importo
                            c+=1
    ''' 
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        if categoria==cat and tipPagamento==tPagamento:
            sommaV+=importo
            c+=1                       
    if (c>0):
        media = sommaV/c
        return(media)
    else:
        return("Errore: nessun elemento trovato")

def venditaMax(tVendite):
    importi = []
    prodottiMax=[]
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        importi.append(importo)
    impMax=max(importi)
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        if importo==impMax:
            prodottiMax.append(prodotto)
    return (impMax,(prodottiMax))

def venditaMinA(tVendite):
    importiA = []
    prodottiMin=[]
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        if reparto=="RepartoA":
            importiA.append(importo)
    impMinA = min(importiA)
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        if importo==impMinA:
            prodottiMin.append(prodotto)
    return (impMinA,(prodottiMin))

def venditaPer(tVendite):
    totA=0
    totB=0
    tot=0
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        tot+=importo
    for (reparto,categoria),(prodotto,(tipPagamento,importo)) in tVendite:
        if reparto=="RepartoA":    
            totA+=importo
        if reparto=="RepartoB":
            totB+=importo
    print("Totale: ",tot)
    print("Reparto A: ",totA*100/tot)
    print("Reparto B: ",totB*100/tot)

tupla_vendite = (
    (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
    (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
    (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
    (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
    (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
    (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
    (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
    (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
)

print("Media globale: ",media_globale(tupla_vendite))

categoria = input("Inserisci categoria: ")
tPagamento = input("Inserisci tipologia pagamento (contanti / carta di credito): ")

while(tPagamento!="contanti" and tPagamento!="carta di credito" and tPagamento!="N/D"):
    tPagamento = input("Reinserisci tipologia pagamento (contanti / carta di credito): ")
print("Importo medio dei dati scelti: ",media(tupla_vendite,categoria,tPagamento))

print("Vendita/e Massima/e: ",venditaMax(tupla_vendite))
print(f"Vendita/e Minima/e nel reparto A: {venditaMinA(tupla_vendite):.2f} %")

print(f"Percentuale vendite per reparto: {venditaPer(tupla_vendite):.2f} %")