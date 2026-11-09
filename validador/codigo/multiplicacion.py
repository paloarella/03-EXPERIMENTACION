
from fractions import Fraction
from math import gcd


# ==========================================
# 1. VALIDAR SIMPLIFICACION CRUZADA
# ==========================================

def validar_simplificacion_cruzada(
    numerador1,
    denominador1,
    numerador2,
    denominador2,
    n1_estudiante,
    d1_estudiante,
    n2_estudiante,
    d2_estudiante
):
    """
    Comprueba que se hayan simplificado los factores
    entre numeradores y denominadores opuestos.
    """

    if min(
        numerador1, numerador2,
        denominador1, denominador2
    ) <= 0:
        return {
            "valido": False,
            "mensaje": "Los valores deben ser enteros positivos."
        }

    divisor1 = gcd(numerador1, denominador2)
    divisor2 = gcd(numerador2, denominador1)

    n1_correcto = numerador1 // divisor1
    d2_correcto = denominador2 // divisor1

    n2_correcto = numerador2 // divisor2
    d1_correcto = denominador1 // divisor2

    simplificacion_correcta = (
        n1_estudiante == n1_correcto
        and d1_estudiante == d1_correcto
        and n2_estudiante == n2_correcto
        and d2_estudiante == d2_correcto
    )

    if simplificacion_correcta:
        return {
            "valido": True,
            "mensaje": "La simplificacion cruzada es correcta."
        }

    return {
        "valido": False,
        "mensaje": (
            "Revisa la simplificacion cruzada. "
            "Debes simplificar entre numeradores y denominadores opuestos."
        )
    }


# ==========================================
# 2. VALIDAR PRODUCTO
# ==========================================

def validar_producto(
    numerador1,
    denominador1,
    numerador2,
    denominador2,
    numerador_resultado,
    denominador_resultado
):
    """
    Comprueba el resultado de una multiplicacion
    de fracciones.
    """

    if min(denominador1, denominador2, denominador_resultado) <= 0:
        return {
            "valido": False,
            "mensaje": "Los denominadores deben ser positivos."
        }

    resultado_correcto = (
        Fraction(numerador1, denominador1)
        * Fraction(numerador2, denominador2)
    )

    resultado_estudiante = Fraction(
        numerador_resultado,
        denominador_resultado
    )

    if resultado_estudiante != resultado_correcto:
        return {
            "valido": False,
            "mensaje": "El producto de las fracciones es incorrecto."
        }

    if (
        resultado_correcto.numerator != numerador_resultado
        or resultado_correcto.denominator != denominador_resultado
    ):
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": "El producto es correcto, pero falta simplificar."
        }

    return {
        "valido": True,
        "mensaje": "La multiplicacion es correcta."
    }


# ==========================================
# 3. PRUEBAS DEL MODULO
# ==========================================

if __name__ == "__main__":

    print("\n========== M01: SIMPLIFICACION CRUZADA ==========")

    print(validar_simplificacion_cruzada(
        1, 5,
        5, 6,
        1, 1,
        1, 6
    ))

    print("\n========== M02: PRODUCTO CORRECTO ==========")

    print(validar_producto(
        1, 1,
        1, 6,
        1, 6
    ))

    print("\n========== M03: PRODUCTO SIN SIMPLIFICAR ==========")

    print(validar_producto(
        1, 5,
        5, 6,
        5, 30
    ))

    print("\n========== M04: SIMPLIFICACION INCORRECTA ==========")

    print(validar_simplificacion_cruzada(
        1, 5,
        5, 6,
        1, 5,
        5, 6
    ))

    print("\n========== M05: PRODUCTO INCORRECTO ==========")

    print(validar_producto(
        1, 5,
        5, 6,
        2, 6
    ))
