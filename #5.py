#5.	Faça um programa que recebe um número em Pés, faça as conversões a seguir e mostre os resultados.
# - 	Polegadas;
# - 	Jardas;
# - 	Milhas;

# Sabe –se que:
# 1 Pé = 12 polegadas;
# 1 Jarda = 3 Pés;
# 1 Milha = 1760 Jarda;

pe = float(input(f'Insira o valor em pés: '))
polegada = pe*12
jarda = pe/3
milha = jarda/1760

print(f'O valor em Polegadas é: {polegada};')
print(f'O valor em Jarda é: {jarda};')
print(f'O valor em Milha é: {milha};')
