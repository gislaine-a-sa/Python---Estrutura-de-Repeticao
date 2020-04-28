print (' Estrutura de Repetição - Exercício 03 MODIFICADO')

paisA = float (input('Informe a população do primeiro país:'))
taxaA = float (input ('Informe a taxa anual de crescimento do primeiro pais (em porcentagem %):'))
paisB = float (input('Informe a população do segundo país:'))
taxaB = float (input ('Informe a taxa anual de crescimento do segundo pais (em porcentagem %):'))
anos = 0
while (paisA < paisB):
    anos += 1
    paisA = paisA + (paisA * (taxaA/100))
    paisB = paisB + (paisB * (taxaB/100))
print ('Após %i anos, o pais A se igualará ou ultrapassará o pais B em número de habitantes' %anos)
print ('Pais A: %.0f' %paisA)
print ('País B: %.0f' %paisB)
