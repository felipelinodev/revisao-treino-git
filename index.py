#calcular quadrado...
def calcular_quadrado(n = 0, lista = []):
    if len(lista) > 0:
        lista_quadrado = []
        for e in lista:
            lista_quadrado.append(e*e)
        return lista_quadrado
    return n*n

#Algoritmo_ordenação
def lista_ordenacao(arr):
    lista_ordenada = sorted(arr)
    return lista_ordenada
