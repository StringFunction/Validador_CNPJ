import random
import math
def gerador_cnpj() -> True:
    """
    Valida um CNPJ com base nos dígitos verificadores.
    Parâmetro:
        cnpj (str): CNPJ com 14 dígitos numéricos.
    Retorno:
        bool: True se válido, False caso contrário.
    """
    

    numero_aleatorio = str(random.randrange(10_000_000, 100_000_000)) + "0001"

    
    # Pesos para cálculo dos dígitos verificadores

    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo  = [6] + pesos_primeiro

    # ------ Função auxiliar para calcular dígito ------

    # Calcula os dois dígitos
    primeiro_digito = calcular_digito(numero_aleatorio[:12], pesos_primeiro)
    numero_aleatorio = numero_aleatorio + str(primeiro_digito)
    segundo_digito  = calcular_digito(numero_aleatorio[:13], pesos_segundo)


    return f"{numero_aleatorio}{segundo_digito}"



def calcular_digito(numero, pesos):
    soma = sum(int(n) * p for n, p in zip(numero, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto
if __name__ == "__main__":
    print(gerador_cnpj())
