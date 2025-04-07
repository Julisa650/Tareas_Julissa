 #Creamos el archivo utilizando 'with open'
with open("my_notes.txt", "w") as escribir:
    # Escribimos texto en el archivo
    print("Hola mundo", file=escribir)
    print("Estamos aprendiendo a escribir archivos en Python", file=escribir)
    print("Aprenderemos a escribir y visualizar", file=escribir)

# La sentencia 'with' cierra automáticamente el archivo al salir del bloque