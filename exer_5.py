def calculadora(a,b,operacao):

    if operacao == "+":
        soma = a + b
        print(soma)
    elif operacao == "-":
        subtracao = a-b
        print(subtracao)
    elif operacao == "*":
        multiplicacao = a * b
        print(multiplicacao)
    elif operacao == "/":
        divisao = a / b
        print(divisao)

calculadora(5,8,"+")
calculadora(5,8,"-")
calculadora(5,8,"*")
calculadora(5,8,"/")