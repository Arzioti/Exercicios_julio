# 8.	Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence,
#  de acordo com a tabela abaixo;

# Faixa etária	    Classificação
# <12	            Criança
# 13~17	            Adolescente
# 18^59	            Adulto
# >60	            Especialista

idade = int(input(f'Insira a idade do individuo: '))

if idade < 12:
    print('Criança')
elif idade >=13 and idade <=17:
    print('Adolescente')
elif idade >=18 and idade <=59:
    print('Adulto')
elif idade >=60:
    print('Especialista')