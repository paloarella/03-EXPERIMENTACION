from fractions import Fraction
from hypothesis import given, settings, strategies as st

from validador.codigo.tecnicas_fracciones import (
    multiplicar_fracciones,
    convertir_mixta_a_impropia,
    convertir_impropia_a_mixta,
)

# Prueba 1: la multiplicación debe conservar
# el valor matemático de las fracciones.
@settings(max_examples=200)
@given(
    n1=st.integers(min_value=0, max_value=10000),
    d1=st.integers(min_value=1, max_value=10000),
    n2=st.integers(min_value=0, max_value=10000),
    d2=st.integers(min_value=1, max_value=10000),
)
def probar_multiplicacion(n1, d1, n2, d2):

    resultado = multiplicar_fracciones(n1, d1, n2, d2)

    obtenido = Fraction(
        resultado["resultado_numerador"],
        resultado["resultado_denominador"]
    )

    esperado = Fraction(n1, d1) * Fraction(n2, d2)
    assert obtenido == esperado

# Prueba 2: convertir una mixta a impropia
# debe conservar su valor.
@settings(max_examples=200)
@given(
    entero=st.integers(min_value=0, max_value=10000),
    denominador=st.integers(min_value=1, max_value=10000),
    numerador=st.integers(min_value=0, max_value=9999),
)
def probar_conversion_mixta(entero, denominador, numerador):
    numerador = numerador % denominador

    resultado = convertir_mixta_a_impropia(
        entero, numerador, denominador
    )

    original = Fraction(entero * denominador + numerador, denominador)

    convertido = Fraction(
        resultado["numerador"],
        resultado["denominador"]
    )

    assert original == convertido


# Prueba 3: convertir una impropia a mixta
# debe conservar su valor.
@settings(max_examples=200)
@given(
    numerador=st.integers(min_value=0, max_value=100000),
    denominador=st.integers(min_value=1, max_value=10000),
)
def probar_conversion_inversa(numerador, denominador):

    resultado = convertir_impropia_a_mixta(
        numerador, denominador
    )

    reconstruida = (
        Fraction(resultado["entero"], 1)
        + Fraction(
            resultado["numerador"],
            resultado["denominador"]
        )
    )

    original = Fraction(numerador, denominador)
    assert reconstruida == original


if __name__ == "__main__":
    probar_multiplicacion()
    print("Multiplicación: aprobada.")

    probar_conversion_mixta()
    print("Conversión mixta a impropia: aprobada.")

    probar_conversion_inversa()
    print("Conversión impropia a mixta: aprobada.")

    print("\nTodas las propiedades se comprobaron correctamente.")
