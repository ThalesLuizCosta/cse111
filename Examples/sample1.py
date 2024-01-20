# Importe a função sleep do módulo de tempo, para que a função sleep possa ser usada neste programa.
from time import sleep

# Solicite que o usuário insira seu nome.
name = input("Hello! What's your name? ")

# Imprima os números 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)

# Use "f-string" do Python para formatar uma saudação para o usuário e, em seguida, imprimir a saudação.
print(f"Welcome to CSE111, {name}!")