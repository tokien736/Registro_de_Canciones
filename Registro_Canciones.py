canciones = {
    "Cantante" : [],
    "Album" : [],
    "Año" : [],
    "Autor" : []
}
def insertar():
    tamaño = int(input("Cuantas canciones Ingresaras: "))
    for i in range(tamaño):
        cantate = input("Ingrese el Cantante {}: \t".format(i+1))
        album = input("Ingrese el Album {}: \t".format(i+1))
        año = input("Ingrese el Año {}: \t".format(i+1))
        autor = input("Ingrese el Autor {}: \t".format(i+1))
        canciones["Cantante"].append(cantate)
        canciones["Album"].append(album)
        canciones["Año"].append(año)
        canciones["Autor"].append(autor)
    print(canciones)
    

while True:
    print("----Registro de canciones---\n")
    print("1. Insetar cancion\n")
    print("2. Modificar cancion\n")
    print("3. Eliminar cancion\n")
    print("4. Eliminar cancion\n")

    opcion =str(input("Escoja una opcion:"))
    if opcion == "1":
        insertar()
    elif opcion == "2":
        print("opcion 2")
    elif opcion == "2":
        print("opcion 3")
    elif opcion == "3":
        print("opcion 3")
    elif opcion == "4":
        break

