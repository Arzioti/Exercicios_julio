# 6.	Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, 
#       sabendo-se que:

# Salário < R$ 1000,00 aumento de 25%.
# Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
# Salário >= R$ 2000,00 aumento de 10%.

salario = float(input(f'Digite o salário do funcionário: '))


if salario < 1000:
    novo_salario = salario*1.25
    print(f'O salário é {novo_salario}')
elif salario >= 1000 and salario < 2000:
    novo_salario = salario*1.15
    print(f'O salário é {novo_salario}')
elif salario >= 2000:
    novo_salario = salario*1.1
    print(f'O salário é {novo_salario}')    