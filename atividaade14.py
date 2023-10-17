# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("digite seu salario :"))
if salario > 1250.00:
    ajuste= salario * 0.10

else:
    ajuste = salario + 0.15
novo_salario = salario + ajuste

print(f"Seu novo salário com o aumento é: R${novo_salario:.2f}")

