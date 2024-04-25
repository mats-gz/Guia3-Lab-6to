def mathsOper(num1, num2):
    resultados = []

    suma = num1 + num2
    resta = num1 - num2
    div = num1 / num2
    mult = num1 * num2

    resultados.append(suma)
    resultados.append(resta)
    resultados.append(div)
    resultados.append(mult)

    return resultados

print(f"Los resultados de las operaciones matematícas realizadas con los numeros ingresados son:", mathsOper(2,2))
