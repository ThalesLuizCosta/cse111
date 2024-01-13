# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
Você trabalha para uma loja de varejo que quer aumentar as vendas na terça-feira e quarta-feira, que são os dias de vendas mais lentas da loja. Na terça-feira e quarta-feira, se o subtotal de um cliente for maior que US$ 50, o loja vai descontar a compra do cliente em 10%.
"""

# Importe o módulo datatime para que ele possa ser usado neste programa.
from datetime import datetime

# A taxa de desconto é de 10% e a taxa de imposto sobre vendas é de 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

subtotal = 0

print("Enter the price and quantity for each item.")
price = 1
while price != 0:
    # Obtenha o preço do usuário.
    price = float(input("Please enter the price: "))
    if price != 0:
        # Obtenha a quantidade do usuário.
        quantity = int(input("Please enter the quantity: "))

        subtotal += price * quantity

        # Imprima uma linha em branco.
        print()

# Arredondar o subtotal para dois dígitos após o decimal e imprimir o subtotal.
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}")
print()

# Chame o método now() para obter a data e a hora atuais como um objeto datetime do sistema operacional do computador.
current_date_and_time = datetime.now()

# Chame o método weekday() para obter o dia da semana do objeto current_date_and_time.
weekday = current_date_and_time.weekday()

# se o subtotal for maior que 50 e hoje for terça ou quarta-feira, calcule o valor do desconto.
if weekday == 1 or weekday == 2:
    if subtotal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add"
                f" {lacking:.2f} to your order.")
    else:
        discount = round(subtotal * DISC_RATE, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

# Calcule o imposto sobre vendas. Observe que calculamos o imposto depois de calcular o desconto porque o cliente não paga imposto sobre o preço cheio, mas sobre o preço com desconto.
sales_tax = round(subtotal * SALES_TAX_RATE, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

# Calcule o total adicionando o subtotal e o imposto sobre vendas.
total = subtotal + sales_tax

# Exiba o total para o usuário ver.
print(f"Total: {total:.2f}")
