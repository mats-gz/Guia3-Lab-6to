lista_tareas = []

def agregar_tareas(lista_tareas):
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

def mostrar_tareas(lista_tareas):
    if lista_tareas == []:
        print("No hay tareas en la lista.")
    else:
        for tareas in lista_tareas:
            for tarea, valor in tareas.items():
                print(f"{tarea} : {valor}")

def completar_tarea(lista_tareas):
    tarea = int(input("Ingrese el número de la tarea que desea marcar como completa:"))
    tarea -= 1
    if tarea in range(len(lista_tareas)):
        print("Marcando la tarea como completa...")
        lista_tareas.pop(tarea)
    else:
        print("Número de tarea ingresado no existente, ingrese otro número")

def menu_opciones():
    print("Elija una de las opciones:")
    print("1. Agregar tareas")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completa")
    print("4. Salir del menú")

def mostrar_menu():
    while True:
        menu_opciones()
        opcion = input("Ingrese su elección:")

        if opcion == "1":
            agregar_tareas(lista_tareas)
        elif opcion == "2":
            mostrar_tareas(lista_tareas)
        elif opcion == "3":
            completar_tarea(lista_tareas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break

mostrar_menu()