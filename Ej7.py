lista_tareas = []
def agregar_tareas():
    tarea = {"Tarea" : "", "Fecha límite": "", "Prioridad": ""}
    for i, j in tarea.items():
        if i == "Tarea":
            j = input("Ingrese el nombre de la tarea:")
            tarea["Tarea"] = j
        if i == "Fecha límite":
            j = input("Ingrese la fecha de la tarea:")
            tarea["Fecha límite"] = j
        if i == "Prioridad":
            j = input("Ingrese la prioridad de la tarea:")
            tarea["Prioridad"] = j
    lista_tareas.append(tarea)
    print(tarea)
    print("Tarea agregada exitosamente")

def mostrar_tareas():
    if lista_tareas == []:
        print("No hay tareas en la lista.")
    else:
        for tareas in lista_tareas:
            for tarea, valor in tareas.items():
                print(f"{tarea} : {valor}")

def menu_opciones():
    print("Elija una de las opciones:")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. Salir del menú")

def mostrar_menu():
    while True:
        menu_opciones()
        opcion = input("Ingrese su elección:")

        if opcion == "1":
            agregar_tareas()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break

mostrar_menu()