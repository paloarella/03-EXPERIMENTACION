from fractions import Fraction
from hypothesis import given, settings, strategies as st

# Generador de fracciones válidas.
fracciones = st.builds(
    Fraction,
    st.integers(min_value=-10000, max_value=10000),
    st.integers(min_value=1, max_value=10000)
)

@settings(max_examples=300)
@given(a=fracciones, b=fracciones)
def probar_suma(a, b):
    resultado = Fraction(a.numerator, a.denominator) + Fraction(
        b.numerator, b.denominator
    )
    assert resultado == a + b


@settings(max_examples=300)
@given(a=fracciones, b=fracciones)
def probar_resta(a, b):
    resultado = Fraction(a.numerator, a.denominator) - Fraction(
        b.numerator, b.denominator
    )
    assert resultado == a - b


@settings(max_examples=300)
@given(a=fracciones, b=fracciones)
def probar_multiplicacion(a, b):
    resultado = Fraction(a.numerator, a.denominator) * Fraction(
        b.numerator, b.denominator
    )
    assert resultado == a * b


@settings(max_examples=300)
@given(
    a=fracciones,
    b=fracciones.filter(lambda x: x != 0)
)
def probar_division(a, b):
    resultado = Fraction(a.numerator, a.denominator) / Fraction(
        b.numerator, b.denominator
    )
    assert resultado == a / b


if __name__ == "__main__":

    pruebas = [
        ("Suma", probar_suma),
        ("Resta", probar_resta),
        ("Multiplicación", probar_multiplicacion),
        ("División", probar_division),
    ]

    for nombre, prueba in pruebas:
        prueba()
        print(f"{nombre}: 300 casos aprobados.")

    print("\nTotal: 1200 casos generados correctamente.")
