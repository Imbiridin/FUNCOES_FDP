def contar_vogais(texto):

    contagem = 0
    vogais = ("aeiou").lower()

    for vogal in texto:

        if vogal in vogais:
            contagem += 1

    if contagem > 0:
        print(contagem)
    else:
        print("Não tem vogal")

contar_vogais("python")