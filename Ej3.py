def countPalabras(texto):
    palabras = texto.split()
    cantidad = len(palabras)
    return cantidad

print(f"La cantidad de palabras presente en tu texto es: {countPalabras("Soy la ariane")}")