# 11.	Escreva um algoritmo para exibir o nome do lanche a partir da entrada do número do 
#       mesmo pelo usuário, de acordo com a tabela abaixo:

# Nr. 	                Lanche
# 1	                    Big Mac
# 2	                    Quarteirão
# 3	                    McChicken
# 4	                    Cheddar McMelt
# 5	                    McMax


lanche = ['Big Mac','Quarteirão','McChicken','Cheddar McMelt','McMax']

n_lanche = int(input(f'Qual o número do lanche: '))
n_lanche = n_lanche-1


if n_lanche >0 and n_lanche<5:
    print(f'O lanche foi o {lanche[n_lanche]}')
else:
    print(f'Lanche não cadastrado!')