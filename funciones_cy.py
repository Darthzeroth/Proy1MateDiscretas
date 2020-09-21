import collections

#reflexiva
def is_reflexive(relacion, set):
    faltantes = []
    for elemento in set:
        if (elemento, elemento) not in relacion:
            faltantes.append((elemento,elemento))          
    if (len(faltantes) <= 0):
        print ("REFLEXIVA: aRa, para todo elemento del conjunto")
        return True
    else:
        print ("NO REFLEXIVA - PARES FALTANTES:" + str(faltantes))           
        return False

#simetrica
def is_symmetric(relacion):
    faltantes =[]
    for tuplas in relacion:
        if not tuplas[::-1] in relacion:
            faltantes.append(tuplas[::-1])
    if (len(faltantes) <= 0):
        print ("SIMETRICA: aRb -> bRa")
        return True
    else:
        print ("ANTISIMETRICA: aRb -> !bRa") 
        print ("NO SIMETRICA - PARES FALTANTES:" + str(faltantes))           
        return  False 
'''        
#antisimetrica
def is_antisymmetric(relacion):
    for a, b in relacion:
        if (a,b) in relacion and (b,a) in relacion and a != b:
            return False
    return True
'''

#transitiva
def is_transitive(relacion):
    faltantes = []
    for a,b in relacion:
        for c,d in relacion:
            if b == c and ((a,d) not in relacion):
                faltantes.append((a,d))
    if (len(faltantes) <= 0):
        print ("TRANSITIVA: aRb, bRc por lo tanto aRc")
        return True
    else:
        print ("NO TRANSITIVA - PARES FALTANTES:" + str(faltantes))           
        return False


#orden parcial
def parcial (set,relacion):
    if (is_reflexive(relacion, set) == True) and (is_symmetric(relacion) == False) and (is_transitive(relacion) == True):
        return True         
    else:
        return False

def is_parcial_order(relacion, set):
    if (parcial (set,relacion) == True):
        print (" ")
        print ("RELACIÓN DE ORDEN PARCIAL: reflexiva + antisimetrica + transitiva")
        
    elif (parcial (set,relacion) == False):
        print (" ")
        print ("RELACIÓN NO ES ORDEN PARCIAL: hay que cumplir que sea reflexiva + antisimetrica + transitiva")
         


#equivalencia
def equiv (relacion, set):
    if (is_reflexive(relacion, set) == True) and (is_symmetric(relacion) == True) and (is_transitive(relacion) == True):
        return True         
    else:
        return False

def is_equivalence(set, relacion):
    if (equiv (relacion, set) == True):
        print ("RELACIÓN DE EQUIVALENCIA: reflexiva + simetrica + transitiva")
        print ("CLASES DE EQUIVALENCIA: ")
        particion = []
        clases = []
        for elemento in set:
            for par in relacion:
                if elemento in par:
                    for x in par:
                        if (x not in clases):
                            clases.append(x)
            print ("["+ str(elemento) +"] = " + "{"+ str(clases) + "}")
            clases = order(clases)
            if (clases not in particion):
                particion.append(clases)
            clases = []
        print("PARTICIONES:"+ particion)
        
    elif (equiv (set,relacion) == False):
        print (" ")
        print ("RELACIÓN NO ES DE EQUIVALENCIA: hay que cumplir que sea reflexiva + simetrica + transitiva")
         










def order(vector):
    for i in range(1, len(vector)):
        x = vector[i]
        j = i - 1
        while(x < vector[j] and j >= 1):     
            vector[j + 1] = vector[j]
            j = j - 1
        if vector[j] <= x:
            vector[j + 1] = x
        else:
            vector[j + 1] = vector[j]
            vector[j] = x
    return vector