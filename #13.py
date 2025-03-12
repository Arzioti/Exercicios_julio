# 13.	Faça um programa que receba 3 valores e verifique se eles podem representar os 
#       lados em um triângulo;

# Nome	                        Característica
# Equilátero	                3 lados iguais
# Isósceles	                    2 lados iguais
# Escaleno	                    3 lados diferente

# Lembre-se que para formar um triângulo, nenhum dos lados pode ser igual a zero e cada um dos 
#       lados precisa ser menor que a soma dos outros dois


l1 = int(input('Digite o primeiro valor: '))
l2 = int(input('Digite o segundo valor: '))
l3 = int(input('Digite o terceiro valor: '))

if l1 < l2 + l3:
    print ('E possível formmar um triangulo retângulo')
elif l2 < l1 + l3:
    print ('E possível formmar um triangulo retângulo')
elif l3 < l1 + l2:
    print ('E possível formmar um triangulo retângulo')
else: print('Não é possivel formar um triângulo retângulo')