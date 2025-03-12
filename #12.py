# 12.	Escreva um algoritmo que a partir da massa e da altura informados pelo usuário, calcule e 
#       apresente seu IMC e sua classificação conforme a tabela abaixo:

# IMC	                Classificação
# < 18	                Magreza
# 18 ~ 24,9	            Saudável
# 25 ~ 29,9	            Sobrepeso
# >= 30	                Obesidade

#IMC = PESO / ALTURA**2

peso = float(input(f'Digite o peso: '))
altura = float(input(f'Digite o altura: '))
imc = peso/altura**2

if imc < 18:
    print(f'Classificação: Magreza')
elif imc>=18 and imc<=24.9:
    print(f'Classificação: Saudável')
elif imc>=25 and imc<=29.9:
    print(f'Classificação: Sobrepeso')
elif imc >= 30:
    print(f'Classificação: Obesidade')