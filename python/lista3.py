print('Lista 1 de exercícios do professor Lauro')

"""
print("Ex1 Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas.")

num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))

print(f'Os valores invertidos dos números são: {num2} e {num1}')

print("EX2 Ler um número inteiro e imprimir seu sucessor e seu antecessor.")

num = int(input('Digite um número e vou lhe mostrar seu sucessor e antecessor. Valendo!  '))

print(f'O número digitado foi {num}. Seu sucessor é {num + 1} e seu antecessor é {num - 1}.')

print("EX3 Faça um programa que leia um valor de conta de restaurante, representando o gasto realizado pelo cliente e imprimir o valor total a ser pago, considerando que o restaurante cobra 10% de taxa de serviço do garçom.")

ent = float(input("Digite o valor da entrada: "))
ptp = float(input("Digite o valor do prato principal: "))
beb = float(input("Digite o valor da bebida: "))
sob = float(input("Digite o valor da sobremesa: "))

conta = ent + ptp + beb + sob
print(f'O valor da sua conta é: R$ {conta} \n')

gar = conta * 0.10
print(f'Cobramos 10% de taxa de serviços, custando: R$ {gar:.2f} \n')

total = conta + gar
print(f'O valor total da comanda é: R$ {total:.2f}')
print("Agradecemos a preferência, volte sempre!")

print("Ex4 Entrar com o raio de um círculo, calcular e imprimir seu perímetro e sua área.")
print("OBS: P = 2 * (pi) * raio e A = (pi) * raio * raio. Use pi = 3.14.")
# (pi) foi usado pois não apareceu seu simbolo e fiquei com preguiça de arrumar isso :)

raio = float(input("Digite o valor do raio: "))

p = 2 * 3.14 * raio
print(f'O perímetro é: {p:.1f}')

a = 3.14 * raio * raio
print(f'A área é: {a:.1f}')

print("Ex5 Ler uma temperatura em graus Centígrados e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5. Onde F é a temperatura em Fahrenheit e C é a temperatura em Centígrados.")

temp = float(input('Digite a temperatura em graus Celsus: '))

conv = (9 * temp + 160) / 5
print(f'A temperatura convertida em Fahrenheit é: {conv:.2f}')

print(f'Ex6 Deseja-se calcular a conta de consumo de energia elétrica de um consumidor. Para isto, escreva um programa que leia o código do consumidor, o preço do KW e a quantidade de KW consumido, e exiba o código do consumidor e o total a pagar.- total a pagar = preço x quantidade - total a pagar mínimo = R$ 21,23')

consumidor = int(input('Digite o valor do cod. do consumidor: '))
preco = float(input('Digite o preço do KW informado no canto superior direito da pag. 1: '))
qtde = float(input('Digite o consumo informado no canto esquerdo inferior da pag. 1: '))
min = 21.23
total = preco * qtde

if total <= min:
    print(f'O valor da fatura é: R$ {min}')
else:
    print(f'O valor da fatura é: R$ {total:.2f}')

print("Ex7 Receber dois números reais e imprimir na tela o maior entre eles. Se ambos forem iguais, deve ser exibida uma mensagem na tela.")

num1 = float(input("Digite um valor real: "))
num2 = float(input("Digite outro valor real: "))

if num1 > num2:
    print(f'Identificamos que o maior valor é: {num1}')
elif num1 < num2:
    print(f'Identificamos que o maior valor é: {num2}')
elif num1 == num2:
    print(f'Os valores digitados são iguais.')
    
print("Ex8 - Entrar com nota da AV1 e nota da AV2 de um aluno. Imprimir: nota de cada AV, média e uma das mensagens: AP se média >= 6, RP se média < 5 ou AV3 se media >=5 e media <6 (a média é 6.0 para aprovação).")

print("Sistema que calcula suas notas e mostra se está aprovado ou se vai fazer av3")

av1 = float(input("Qual foi a nota da sua AV1? "))
av2 = float(input("Qual foi a nota da sua AV2? "))
media = (av1 + av2) / 2

print(f'Sua nota na av1 foi {av1} e na av2 foi {av2}. Sua média é: {media:.1f}. Portanto...')

if media >= 6:
    print("Você está aprovado!")
elif media < 5:
    print("Você está reprovado!")
elif media >= 5 and media < 6:
    print("Você não aprovou desta vez, mas terá uma nova oportunidade na av3!!")

print(f'Ex9 Ler três números a partir do teclado e apresentá-los em ordem decrescente.')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))

if num1 > num2 and num2 > num3:
    print(f'Os numeros exibidos em forma decrescente são: {num1}, {num2}, {num3}')
elif num1 < num2 and num2 < num3:
    print(f'Os numeros exibidos em forma decrescente são: {num3}, {num2}, {num1}')
elif num2 > num1 and num1 > num3:
    print(f'Os numeros exibidos em forma decrescente são: {num2}, {num1}, {num3}')
elif num2 > num1 and num1 < num3:
    print(f'Os numeros exibidos em forma decrescente são: {num2}, {num3}, {num1}')
elif num1 > num3 and num2 < num3:
    print(f'Os numeros exibidos em forma decrescente são: {num1}, {num3}, {num2}')
elif num1 < num3 and num1 > num2:
    print(f'Os numeros exibidos em forma decrescente são: {num3}, {num1}, {num2}')
elif num1 == num2 and num2 == num3:
    print(f'AHHHHHH eu sabia que vc ia tentar isso hahahahahahahahahahhaa. Vou chamar Marcos Bras pra morder sua virilha!')



"""

print(f'Ex10  Faça um programa que simule um calculador de 4 operações. Seu programa deverá ler dois números e o operador e efetuar os cálculos, exibindo o resultado final. O programa deve ser capaz de verificar operações inválidas.')

num1 = int(input('Digite um número inteiro: '))
operacao = input('Qual operação deseja? Digite "+", "-", "/" ou "*":  ')
num2 = int(input('Digite um número inteiro: '))
res = 0



if operacao == '+':
    res = num1 + num2
    print(f'O resultado da operação escolhida é: {res}')
elif operacao == '-':
    res = num1 - num2
    print(f'O resultado da operação escolhida é: {res}')
elif operacao == '/':
    res = num1 / num2
    print(f'O resultado da operação escolhida é: {res}')
elif operacao == '*':
    res = num1 * num2
    print(f'O resultado da operação escolhida é: {res}')
else:
    res = 'Operação invalida'
    print(res)

