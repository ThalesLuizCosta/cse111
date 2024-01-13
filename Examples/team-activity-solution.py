# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""

# Importe o módulo datatime para que ele possa ser usado neste programa.
from datetime import datetime

# A taxa de desconto é de 10% e a taxa de imposto sobre vendas é de 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

# Obtenha o subtotal do usuário.
subtotal = float(input("Please enter the subtotal: "))

# Chame o método now() para obter a data e a hora atuais como um objeto datetime do sistema operacional do computador.
current_date_and_time = datetime.now()

# Chame o método weekday() para obter o dia da semana do objeto current_date_and_time.
weekday = current_date_and_time.weekday()

# Se o subtotal for maior que 50 e hoje for terça ou quarta-feira, calcule o valor do desconto.
if subtotal >= 50 and (weekday == 1 or weekday == 2):
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
