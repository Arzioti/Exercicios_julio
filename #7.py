#7. Faça um programa que receba o mês em número e apresente-o por extenso.

# import calendar

# mes = int(input(f'Insira o número do mês: '))
# print(f'O mês é: {calendar.month_name[mes]}')


meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outrubro','Novembro','Dezembro']
mes = int(input(f'Insira o número do mês: '))
mes = mes-1
print(f'O nome do mês é: {meses[mes]}.')