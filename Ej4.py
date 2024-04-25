def esPalindromo(texto):
    textInv = ''.join(reversed(texto))
    if texto == textInv:
        return True
    else: 
        return False
    
print("¿La palabra ingresada es palindroma?", esPalindromo("oso"))