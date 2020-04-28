print ('Estrutura de Repitação - Exercício 13')

base=int(input('Informe a base:'))
valor_base=base
expoente=int(input('\nInforme o expoente:'))
if (expoente==1) or (expoente==0):
  if (expoente==1):
     print('\nResultado: %s' % (base))
  else:
    print('\nResultado: 1')
else:
  for i in (range(expoente-1)):
    base*=valor_base
  print('\nResultado: %s' % (base))
