# Abrimos el archivo txt y lo manejamos con 'with open'
with open("my_notes.txt", "r") as escribir:
    # Leemos la primera línea utilizando readline
    visualizar = escribir.readline()
    print(visualizar)  # Imprimimos la primera línea

    # Usamos un bucle for para recorrer las demás líneas
    for linea in escribir:
        print(linea)  # Imprimimos cada línea
# No es necesario cerrar el archivo, ya que 'with' lo hace automáticamente