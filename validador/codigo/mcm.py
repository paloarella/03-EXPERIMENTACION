
from math import gcd

def calcular_mcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo de dos enteros.
    El resultado siempre es no negativo.
    """
    if type(a) is not int or type(b) is not int:
        raise TypeError("Los valores deben ser enteros.")

    if a == 0 or b == 0:
        return 0
    return abs((a // gcd(a, b)) * b)


def validar_mcm(a: int, b: int, resultado: int) -> bool:
    """
    Comprueba que el resultado corresponda al MCM.
    """
    if type(resultado) is not int:
        return False

    return resultado == calcular_mcm(a, b)
