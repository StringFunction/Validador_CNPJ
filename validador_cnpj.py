def validar_cnpj(cnpj: str) -> bool:
    """
    Valida um CNPJ com base nos dígitos verificadores.
    Parâmetro:
        cnpj (str): CNPJ com 14 dígitos numéricos.
    Retorno:
        bool: True se válido, False caso contrário.
    """

    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return False

    # CNPJ com todos os dígitos iguais é inválido
    if cnpj == cnpj[0] * 14:
        return False

    # Pesos para cálculo dos dígitos verificadores
    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo  = [6] + pesos_primeiro



    # Calcula os dois dígitos
    primeiro_digito = calcular_digito(cnpj[:12], pesos_primeiro)
    segundo_digito  = calcular_digito(cnpj[:13], pesos_segundo)

    # Compara com os últimos dois dígitos do CNPJ
    return cnpj[-2:] == f"{primeiro_digito}{segundo_digito}"


def calcular_digito(numero, pesos):
    soma = sum(int(n) * p for n, p in zip(numero, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


if __name__ == "__main__":
    print(validar_cnpj("18781203 000128"))