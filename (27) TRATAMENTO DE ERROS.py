'''print("início")

assert 2 < 1, "2 Deve ser maior que 1"

print("fim")'''

'''try:
    idade = int(input("Digite sua idade"))
    print("Sua idade é ", idade)
except:
    print("Digite somente números!")'''
try:
    numero = int(input("Digite um número:"))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("DIGITE UM NÚMERO INTEIRO!!")    
except ZeroDivisionError:
    print("NÃO EXISTE DIVISÃO POR ZERO")