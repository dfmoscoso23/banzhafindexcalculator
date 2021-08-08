#calculando
#from tail_recursion import tail_recursive, recurse
partes={
    'unes':49,
    'pachakutik':25,
    'ID':16,
    'PSC':14,
    'Creo':12,
    'independientes':6,
    'AH':2,
    'avanza':2,
    'EU':2,
    'DSI':1,
    'PSP':1,
    'MC25':1,
    'UE':1, 
    'prov':5,
    'presidente':0
}
"""
'unes':48,
    'pachakutik':25,
    'ID':16,
    'PSC':14,
    'Creo':12,
    'independientes':6,
    'AH':2,
    'avanza':2,
    'EU':2,
    'DSI':1,
    'PSP':1,
    'MC25':1,
    'prov':5
    'presidente':0
    'Azuay':5,
    'Bolivar':3,
    'Cañar':3,
    'Carchi':3,
    'Chimborazo':4,
    'Cotopaxi':4,
    'El oro':5,
    'esmeraldas':4,
    'Galápagos':2,
    'guayas':20,
    'Imbabura':4,
    'loja':4,
    'los ríos':6,
    'Manabí':9,
    'Morona santiago':2,
    'Napo':2,
    'Orellana':2,
    'Pastaza':2,
    'pichincha':16,
    'Santa Elena':3,
    'Santo Domingo':4,
    'Sucumbios':3,
    'Tungurahua':4,
    'Zamora chinchipe':2,
    'Nacionales':15,
    'Extranjero':6,
    (votos >=69 and 'Creo'in item)or votos>=92
    (votos >=69 and 'presidente'in item)or votos>=92 
    ((votos >=69 and 'presidente'in coalicionsinelemento)or votos>=92)
"""
    
indiceB={}
indiceBanzhaf={}
lista=[]
listacoaliciones=[]

for item in partes:
    lista.append(item)

def potencia(c):
    if len(c) == 0:
        return [[]]
    r=potencia(c[:-1])   
    return r + [s + [c[-1]] for s in r]

def potencia2(lista, recop):
    if len(lista) == 0:
        a=[[]]
        return a.extend(recop)
    
    return potencia2(lista[:-1] + [s + [lista[-1]] for s in lista[:-1]])
    #return potencia2(lista[:-1],)
    #r=potencia(lista[:-1])   
    #return r + [s + [lista[-1]] for s in r]

def prueba(lista):    
    result=[]
    y=[]
    #y.extend(s)
    conj=[[s] for s in lista[:-1]]
    result.extend(conj)
    print(conj)
    #conj.append(s)
    return result

lista=["l","i","s"]
b=prueba(lista)
print("--")
print(b)

def coalicionesganadoras(l):
    votos=0
    for item in l:
        for parte in item:
            votos+=partes[parte]
        if (votos >=69 and 'Creo'in item)or votos>=92 :
            listacoaliciones.append(item)
        votos=0

def indice(lista, coaliaciones):
    votos=0
    for item in lista:
        indiceB[item]=0
        for coalicion in coaliaciones:
            if item in coalicion:
                coalicionsinelemento=coalicion.copy()
                coalicionsinelemento.remove(item)
                for parte in coalicionsinelemento:
                    votos+=partes[parte]
                if not ((votos >=69 and 'Creo'in coalicionsinelemento)or votos>=92):
                    indiceB[item]+=1
                coalicionsinelemento=[] 
                votos=0
def banzhaf(indice):
    totaltbp=0
    for item, valor in indice.items():
        totaltbp+=valor
    for item, valor in indice.items():
        indiceBanzhaf[item]=valor/totaltbp

#coalicionesganadoras(potencia(lista))
#indice(lista,listacoaliciones)

#banzhaf(indiceB)

#sort=sorted(indiceBanzhaf.items(),key=lambda x:x[1],reverse=True)
#print(sort)
