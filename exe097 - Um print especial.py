def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f"  {txt}")
    print('~' * (len(txt) + 4))


print('Seja bem vindo ao cirador de títulos')
frase1 = str(input('Digite um título: '))
escreva(frase1)
frase2 = str(input('Digite outro título: '))
escreva(frase2)
frase3 = str(input('Digite mais um título: '))
escreva(frase3)
