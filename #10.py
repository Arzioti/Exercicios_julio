# 10.	Escreva um programa que leia a velocidade máxima permitida em uma avenida e velocidade com 
#       que o motorista estava dirigindo nela e calcule a multa que uma pessoa vai receber;

# Siga a tabela de multas

# Velocidade Ultrapassada	    Valor da Multa
# Até 10 km/h	                R$ 50,00
# 11 a 30 km/h	                R$ 100,00
# Mais 31 km/h	                R$ 200,00

# Exemplo: 
# 	Limite: 50 km/h
# 	Velocidade: 59 km/h
# 	Multa: R$ 50,00


velocidade_via = int(input(f'Digite a velocidade da via: '))
velocidade = int(input(f'Digite a velocidade que o motorista estava dirigindo: '))
resultado = velocidade-velocidade_via


if resultado < 10:
    print(f'A multa é de R$ 50,00.')
elif resultado >=11 and resultado <= 30:
    print(f'A multa é de R$ 100,00.')
elif resultado >= 31:
    print(f'A multa é de R$ 200,00.')
