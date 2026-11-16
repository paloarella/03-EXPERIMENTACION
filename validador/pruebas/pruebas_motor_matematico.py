
from fractions import Fraction
from hypothesis import given, settings, strategies as st

from validador.codigo.motor_matematico import operar_fracciones


# Generadores de datos válidos.
numeradores = st.integers(min_value=0, max_value=10000)
denominadores = st.integers(min_value=1, max_value=10000)


# SUMA
@settings(max_examples=200)
@given(
    n1=numeradores,
    d1=denominadores,
    n2=numeradores,
    d2=denominadores
)
def probar_suma(n1, d1, n2, d2):

    obtenido = operar_fracciones(n1, d1, n2, d2, "+")

    esperado = Fraction(n1, d1) + Fraction(n2, d2)

    resultado = obtenido["resultado"]

    assert Fraction(
        resultado["numerador"],
        resultado["denominador"]
    ) == esperado


# RESTA: solo casos cuyo resultado sea no negativo.
@settings(max_examples=200)
@given(
    n1=numeradores,
    d1=denominadores,
    n2=numeradores,
    d2=denominadores
)
def probar_resta(n1, d1, n2, d2):

    fraccion1 = Fraction(n1, d1)
    fraccion2 = Fraction(n2, d2)

    if fraccion1 < fraccion2:
        return

    obtenido = operar_fracciones(n1, d1, n2, d2, "-")

    esperado = fraccion1 - fraccion2

    resultado = obtenido["resultado"]

    assert Fraction(
        resultado["numerador"],
        resultado["denominador"]
    ) == esperado


# MULTIPLICACIÓN
@settings(max_examples=200)
@given(
    n1=numeradores,
    d1=denominadores,
    n2=numeradores,
    d2=denominadores
)
def probar_multiplicacion(n1, d1, n2, d2):

    obtenido = operar_fracciones(n1, d1, n2, d2, "*")

    esperado = Fraction(n1, d1) * Fraction(n2, d2)

    resultado = obtenido["resultado"]

    assert Fraction(
        resultado["numerador"],
        resultado["denominador"]
    ) == esperado


# DIVISIÓN: el numerador de la segunda fracción debe ser positivo.
@settings(max_examples=200)
@given(
    n1=numeradores,
    d1=denominadores,
    n2=st.integers(min_value=1, max_value=10000),
    d2=denominadores
)
def probar_division(n1, d1, n2, d2):

    obtenido = operar_fracciones(n1, d1, n2, d2, "/")

    esperado = Fraction(n1, d1) / Fraction(n2, d2)

    resultado = obtenido["resultado"]

    assert Fraction(
        resultado["numerador"],
        resultado["denominador"]
    ) == esperado


if __name__ == "__main__":

    pruebas = [
        ("Suma", probar_suma),
        ("Resta", probar_resta),
        ("Multiplicación", probar_multiplicacion),
        ("División", probar_division),
    ]

    for nombre, prueba in pruebas:
        prueba()
        print(f"{nombre}: pruebas aprobadas.")

    print("\nTodas las pruebas del motor finalizaron correctamente.")
