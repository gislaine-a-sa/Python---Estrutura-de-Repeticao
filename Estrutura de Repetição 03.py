print (' Estrutura de Repetição - Exercício 03')

nome = str (input ('Informe o nome:'))
while (len(nome) <= 3):
 nome = str (input ('Informe o nome:'))
 idade = int (input('Informe a idade:'))
while (idade>15) or (idade<0):
 idade = int (input ('Informe a idade:'))
salario = float (input ('Informe o salário:'))
while (salario<0):
 salario = floar (input('Informe o salário:'))
sexo = str (input ('Informe o sexo, digite F - Feminino , M - Masculino, ou N - Prefiro não informar'))
while sexo!='F' and sexo!='M' or sexo !='N':
 sexo = str (input ('Informe o sexo, digite F - Feminino , M - Masculino, ou N - Prefiro não informa'))
status = str (input ('Informe o seu estado civil: S - Solteiro, C - Casado, V - Viúvo ou D - Divorciado'))
while status !='S' and status!='C' and status!='V' and status!='D':
 status = str (input ('Informe o seu estado civil: S - Solteiro, C - Casado, V - Viúvo ou D - Divorciado'))    
