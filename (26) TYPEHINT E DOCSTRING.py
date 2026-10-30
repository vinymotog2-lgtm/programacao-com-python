def somar(a: int, b: int) -> int:
    '''
    Função para somar dois números

    Args:
        a (int): número um
        b (int): número dois

    returns:
        int: soma dos dois números      
    '''
    return a + b
print(somar (2, 2))
print(somar("Olá", "mundo"))
#Typehint indica qual tipo de dado deve ser passado
help(somar)