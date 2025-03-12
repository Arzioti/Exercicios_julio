# 9.	Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão,
#       de acordo com a tabela abaixo;

# Código de Profissão	    Ocupação
# 1	                        Matemático
# 2	                        Analista de Sistemas
# 3	                        Físico
# 4	                        Arquiteto
# 5	                        Piloto de Aeronaves


ocupacao = ['Matemático','Analista de Sistemas','Físico','Arquiteto','Piloto de Aeronaves']
codigo = int(input(f'Digite o codigo da profissão: '))
codigo = codigo-1

if codigo >0 and codigo <=4:
    print(f'A ocupação é {ocupacao[codigo]}.')
else:
    print('Ocupação não cadastrada')