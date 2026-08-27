'''import re 
codigo = input("Digite um código!")
if re.fullmatch(r"[a-z0-9]{5}", codigo):
    print("Código válido!")
else:
    print("Código inválido!")'''
import re 

codigo = input("Digite o codigo")

while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Digite o código novamente: ")
    
print("Código aceito!")    



    