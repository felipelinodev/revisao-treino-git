#Algoritmo_ordenação
def lista_ordenacao(arr):
    lista_ordenada = sorted(arr)
    return lista_ordenada


#calcular quadrado...
def calcular_quadrado(n=0, lista = [], order=False):
    if len(lista) > 0:
        lista_quadrado = []
        for e in lista:
            lista_quadrado.append(e*e)
        if order == True:
            return lista_ordenacao(lista_quadrado)
        else:
            return lista_quadrado
    else:
        return n*n
