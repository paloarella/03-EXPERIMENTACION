
from fractions import Fraction
from hypothesis import given, settings, strategies as st
from validador.codigo.motor_matematico import operar_fracciones

numeradores = st.integers(min_value=-100000, max_value=100000)
denominadores = st.integers(min_value=1, max_value=100000)

def comprobar_resultado(obtenido, esperado):
    resultado = obtenido["resultado"]
    fraccion_obtenida = Fraction(
        resultado["numerador"],
        resultado["denominador"]
    )
    assert fraccion_obtenida == esperado


@settings(max_examples=300)
@given(n1=numeradores, d1=denominadores,
       n2=numeradores, d2=denominadores)

def probar_suma(n1, d1, n2, d2):
    obtenido = operar_fracciones(n1, d1, n2, d2, "+")
    esperado = Fraction(n1, d1) + Fraction(n2, d2)
    comprobar_resultado(obtenido, esperado)


@settings(max_examples=300)
@given(n1=numeradores, d1=denominadores,
       n2=numeradores, d2=denominadores)

def probar_resta(n1, d1, n2, d2):
    obtenido = operar_fracciones(n1, d1, n2, d2, "-")
    esperado = Fraction(n1, d1) - Fraction(n2, d2)
    comprobar_resultado(obtenido, esperado)


@settings(max_examples=300)
@given(n1=numeradores, d1=denominadores,
       n2=numeradores, d2=denominadores)

def probar_multiplicacion(n1, d1, n2, d2):
    obtenido = operar_fracciones(n1, d1, n2, d2, "*")
    esperado = Fraction(n1, d1) * Fraction(n2, d2)
    comprobar_resultado(obtenido, esperado)


@settings(max_examples=300)
@given(n1=numeradores, d1=denominadores,
       n2=st.integers(min_value=-100000, max_value=100000)
          .filter(lambda n: n != 0),
       d2=denominadores)

def probar_division(n1, d1, n2, d2):
    obtenido = operar_fracciones(n1, d1, n2, d2, "/")
    esperado = Fraction(n1, d1) / Fraction(n2, d2)
    comprobar_resultado(obtenido, esperado)

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

    print("\nTodas las pruebas del motor general finalizaron correctamente.")
