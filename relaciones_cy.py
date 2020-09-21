from funciones_cy import *


def run(): 
    print("*******************************************************") 
    print("*                                                     *")
    print("* PROGRAMA PARA VALIDAR TIPO DE RELACIÓN DE CONJUNTOS *")
    print("*                                                     *")
    print("*******************************************************") 
    print("\n")
    set = [1,2]
    #relacion = [(1,1),(2,2),(1,2),(1,3),(2,1),(3,3),(3,1),(2,3),(3,2)] #equivalencia
    relacion = [(1,1),(2,2),(1,2)] #parcial
    #relacion = [(1,1), (2,2), (3,3),(4,4),(10,10), (20,20),(1,2)]
    #relacion = [(2,2),(1,2),(2,1),(1,3),(3,3),(3,1)]
    '''
    print("Capturar todos los elementos del conjunto")
    rango = int(input("¿Cuántos elementos tiene el conjunto?"))
    set = []
    for i in range(rango):
        linea = input("Inserte el {}o. elemento: ".format(i+1))
        set.append(int(linea))

    
    print ("Conjunto: ", set, "\n")
    relacion = []
    rango = int(input("¿Cuántos pares ordenados tiene la Relación?"))
    for i in range(rango):
        linea = input("Inserte el {}o. par de números, separados por espacio: ".format(i+1))
        datos = tuple(int(dato) for dato in linea.split())
        relacion.append(datos)

    print ("Conjunto de pares ordenados: ", relacion, "\n")
  
 '''   
    #imprimi tipos de relación
    is_reflexive(relacion,set)
    is_symmetric(relacion)
    is_transitive(relacion)
    print("#####")
    #Equivalencia u Orden Parcial
    is_parcial_order(set,relacion)
    is_equivalence(relacion,set)
    

if __name__ == '__main__':
    run()

    