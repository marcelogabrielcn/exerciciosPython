frase = input('Digite uma frase qualquer: ').lower().strip()
qtd = frase.count('a')
print('A letra "a" aparece no texto {} vezes.'.format(qtd))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.rfind('a')+1))
