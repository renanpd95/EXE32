import os

cont = int(input("Qual o valor da conta? "))
cli = int(input("Qual a Quantidade de clientes? "))
os.system("clear")

#conta acrescentando percentual do garçom
cont1 = 1.10 * cont

#separação do valor que cada cliente pagará
divs = cont1/cli
print ("Valor que será pago por cada cliente é: R$",divs)


