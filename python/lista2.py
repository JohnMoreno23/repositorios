print(f'Olá! Vamos dar inicio a lista 2 de exercicios de Py. Boa sorte! \n')


'''print(f'Questão 1: Faça um Programa que leia três números inteiros e mostre o maior deles. \n')

n1 = int(input(f'Digite o primeiro numero: '))
n2 = int(input(f'Digite o segundo numero: '))
n3 = int(input(f'Digite o terceiro numero: '))

if n1 >= n2 and n1 >= n3:
    print(f'O maior numero que digitou foi: {n1}')

elif n3 >= n2 and n3 >= n1:
    print(f'O maior numero que digitou foi: {n3}')

elif n2 >= n3 and n2 >= n1:
    print(f'O maior numero que digitou foi: {n2}')
'''
'''
print(f'Questão 2: Crie um código em python que peça 2 números inteiros e um número real. Calcule e mostre: ')
print(f'a) o produto do dobro do primeiro com metade do segundo')
print(f'b) a soma do triplo do primeiro com o terceiro ')
print(f'c) o terceiro elevado ao cubo \n')


num1 = int(input(f'Digite um numero: '))
num2 = int(input(f'Digite mais um numero: '))
num3 = float(input(f'Digite mais um numero: '))

lt_A = (num1 *2) + (num2 /2)
print(f'Resposta da letra a) {lt_A}')

lt_B = (num1 *3) + num3
print(f'Resposta da letra b) {lt_B}')

lt_C = num3 ** 3
print(f'Resposta da letra c) {lt_C}')
'''

'''
print(f'Questão 3: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. ● C = 5 * ((F-32) / 9) \n')

tempf = float(input(f'Digite o valor da temperatura em Fahrenheit: '))

tempc = 5 * ((tempf - 32) / 9)

print(f'A temperatura em graus Celsius é: {tempc:.0f} ºC \n')
'''
'''
print(f'Questão 4: Faça um programa que sorteia um número de 0 a 9999 e mostre na tela cada um dos dígitos separadamente.exemplo: unidade: 4 dezena: 3 centena: 8 milhar ')

questão será feita depois
'''
'''
print(f'Questão 5: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar R$7,00 por cada KM acima do limite. ')

vel = int(input(f'Digite a velocidade em que o veículo passou pelo radar: '))

if vel > 80:
    print(f'Multado! Como ultrapassou o limite de velocidade, sua multa foi calculada em: R$ {(vel - 80) *7}')
elif vel <= 80:
    print(f'Parabéns! Foi confirmmado que está dentro do limite de velocidade permitido. Use o cinto de segurança sempre!!')

print(f'Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor. ')

num1 = int(input(f'Digite um número: '))
num2 = int(input(f'Digite mais um número: '))
num3 = int(input(f'Digite o último número: '))

if num1 == num2 and num2 == num3:
    print(f'Você digitou 3 números iguais...')
elif num1 > num2 and num1 > num3 and num2 > num3:
        print(f'O maior número é {num1} e o menor número é: {num3}')
elif num1 < num2 and num1 < num3 and num2 < num3:
        print(f'O maior número é {num3} e o menor número é {num1}')
elif num1 < num2 and num1 < num3 and num2 > num3:
        print(f'O maior número é {num2} e o menor número é {num1}')
elif num1 < num2 and num1 > num3 and num2 > num3:
        print(f'O maior número é {num2} e o menór número é {num3}')
elif num3 > num2 and num2 < num1 and num1 > num3:
        print(f'O maior número é {num1} e o menor número é {num2}')
else:
        print(f'O maior número é {num3} e o menor número é {num2}')

print(f'EX8 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o número é de 15%. ')

funcionario = input('Digite o nome do funcionário: ')
salario = float(input(f'Digite o salário do funcionário: '))
baseA = 1250.00

aumento1 = salario * 0.10
aumento2 = salario * 0.15

novo_salario1 = salario + aumento1
novo_salario2 = salario + aumento2

if salario > baseA:
    print(f'O aumento aplicado foi 10%. O salário do funcionário {funcionario}, será: R${novo_salario1:.2f}.')
elif salario <= baseA:
    print(f'O aumento aplicado foi 15%. O salário do funcionário {funcionario}, será: R${novo_salario2:.2f}.')



'''



print(f'EX6 Faça um programa que leia um ano qualquer e mostre se ele é Bissexto. ')
'''
ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')
'''

print('EX9 Crie um código em python que peça os 3 lados de um triângulo. O script deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno')