#SKU
def fun_sku(titulo, autor, añopub):
    try:
        titulo = titulo[:6]
        autor = autor[:3]
        sku = f"{titulo}-{autor}-{añopub}"
        return sku
    except TypeError:
        print("Complete todos los campos solicitados")


def regist(titulo, autor, añopub, sku): #Funcion registrar
    print()



def menu(): #Funcion Menú
    while True:
        print("Bienvenido a la biblioteca, seleccione una opción para continuar")
        print("1. Registrar libro")
        print("2. Prestar libro")
        print("3. Listar todos los libros")
        print("4. Imprimir reporte de préstamos")
        print("5. Salir del programa")
        op = input()
        if op == "5":
            break
        if op == "1":
            nomlibro = input("Ingrese el nombre de su libro: ")
            nomautor = input("Ingrese el nombre del autor: ")
            añopub = input("Ingrese el año de publicación: ")
            varsku = fun_sku(nomlibro, nomautor, añopub)
            print(varsku)
menu()