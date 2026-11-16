from fractions import Fraction
from validador.codigo.motor_matematico import operar_fracciones

pruebas = [
    (2, -3, 1, 4, "+"),
    (2, 3, 1, -4, "+"),
    (2, -3, 1, 4, "-"),
    (2, -3, 3, 4, "*"),
    (2, 3, 4, -5, "/"),
]

for n1, d1, n2, d2, operador in pruebas:
    obtenido = operar_fracciones(n1, d1, n2, d2, operador)
    resultado = obtenido["resultado"]

    valor = Fraction(
        resultado["numerador"],
        resultado["denominador"]
    )

    esperado = (
        Fraction(n1, d1) + Fraction(n2, d2)
        if operador == "+"
        else Fraction(n1, d1) - Fraction(n2, d2)
        if operador == "-"
        else Fraction(n1, d1) * Fraction(n2, d2)
        if operador == "*"
        else Fraction(n1, d1) / Fraction(n2, d2)
    )

    assert valor == esperado, (
        f"Error en {n1}/{d1} {operador} {n2}/{d2}"
    )

    print(
        f"[APROBADA] {n1}/{d1} {operador} {n2}/{d2}"
        f" = {valor}"
    )

print("\nTodas las pruebas finalizaron correctamente.")