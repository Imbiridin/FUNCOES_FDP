def palindromo(texto):

    texto_invertido = texto[::-1]

    if texto == texto_invertido:
        print("palindromo")
    else:
        print("Não é palindromo")

palindromo("radar")
palindromo("computador")