print('Vamos descobrir se os números são primos ou não?...')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {}, foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('Portanto, esse número é primo.')
else:
    print('Portanto, esse número não é primo.')
