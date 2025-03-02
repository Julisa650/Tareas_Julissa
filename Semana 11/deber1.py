#Creamos la lista bidimensional
lista = [
    [1,2,3],
    [5,6,7],
    [8,9,10]
    ]

#declaramos la funcion buscar con parámetro x (valor que buscará)
def buscar(l, x):
    for i in range(len(l)):  #Iterador i recorre la lista
        for j in range(len(l[i])): #Iterador j recorre las columnas
            if l[i][j] == x:
                return i, j # retornamos ambos iteradores
    return None  # si no encuentra el numero que estamos buscando en la lista retorna None

def mostrar(l, x):  # Creamos otra funcion en la cual vamos a mostrar y pasamos parametros
    listas = buscar(l, x) # Asignamos una variable y le igualamos a nuestra funcion llamada buscar
    if listas is None:  # Si nuestra función mostrar es None quiere decir que no se encontro en la lista el numero
        print("No se encontro")
    else:
        print(f"El numero {x} esta en la posicion {listas} ")  # Si no es None mandamos un print con el numero y la posicion en la lista

print("La lista es: ", lista)

 #Llamamos a la función sin imprimir su retorno
mostrar(lista, 7)