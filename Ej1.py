infPersonal = [
    {"nombre" : "Vicente", "edad" : 17},
    {"nombre" : "Joaquin", "edad" : 17},
    {"nombre" : "Matias", "edad" : 18}
]

diccionario1 = infPersonal[0]
nombre1 = diccionario1["nombre"]
diccionario2 = infPersonal[1]
edad2 = diccionario1["edad"]

print(f"El nombre de la primera persona es: {nombre1}, y la edad de la segunda persona es: {edad2}")

#pt2

for info in infPersonal:
    for clave,valor in info.items():
        print(f"{clave} : {valor}")
