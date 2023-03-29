canciones = {
    "Cantante" : ["Enrique", "Fernando"],
    "Album" : ["rosas", "caramelo"],
    "Año" : [2014, 2016],
    "Autor" : ["Fedrico", "Ruben"]
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
def modificar():
    print(canciones)
    numero = int(input("Ingrese el número de canción a modificar: "))
    cantante = input("Ingrese el nuevo cantante: ")
    album = input("Ingrese el nuevo álbum: ")
    año = input("Ingrese el nuevo año: ")
    autor = input("Ingrese el nuevo autor: ")

    canciones["Cantante"][numero - 1] = cantante
    canciones["Album"][numero - 1] = album
    canciones["Año"][numero - 1] = año
    canciones["Autor"][numero - 1] = autor

    print("La canción ha sido modificada: ")
    print(canciones)

def eliminar():
    print(canciones)
    numero = int(input("Ingrese el número de canción que desea eliminar: "))
    if numero > 0 and numero <= len(canciones["Cantante"]):
        canciones["Cantante"].pop(numero - 1)
        canciones["Album"].pop(numero - 1)
        canciones["Año"].pop(numero - 1)
        canciones["Autor"].pop(numero - 1)
        print("Canción eliminada con éxito.")
    else:
        print("Número de canción inválido.")
    print(canciones)

while True:
    print("----Registro de canciones---\n")
    print("1. Insetar cancion\n")
    print("2. Modificar cancion\n")
    print("3. Eliminar cancion\n")
    print("4. Salir del menú\n")

    opcion =str(input("Escoja una opcion:"))
    if opcion == "1":
        insertar()
    elif opcion == "2":
        modificar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        print("Gracias por Ingresar al Programa")
        break

