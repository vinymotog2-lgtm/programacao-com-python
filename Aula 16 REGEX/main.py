input("digite um número")
import re
codigo = "1234"
if re.fullmatch(r"\d{4}", codigo):
    print("Código aceito!") 
else:
    print("Código negado!")