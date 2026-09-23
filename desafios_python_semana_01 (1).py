# Desafios Python - Semana 01

# 1 - Calculadora de troco
valor_compra = float(input("Valor da compra: "))
valor_pago = float(input("Valor pago: "))

troco = valor_pago - valor_compra

print(f"Troco: R$ {troco:.2f}")


# 2 - Média de notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")


# 3 - Conversor de tempo
segundos = int(input("Digite o tempo em segundos: "))

horas = segundos // 3600
segundos = segundos % 3600

minutos = segundos // 60
segundos = segundos % 60

print(f"{horas}:{minutos}:{segundos}")


# 4 - Calculadora de desconto
preco = float(input("Preço do produto: "))
desconto = float(input("Percentual de desconto: "))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print(f"Preço final: R$ {preco_final:.2f}")


# 5 - Par ou ímpar
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# 6 - Inversor de nome
nome = input("Digite seu nome: ")

nome_invertido = nome[::-1]

print(f"Nome invertido: {nome_invertido}")
