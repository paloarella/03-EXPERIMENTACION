
from fractions import Fraction
from math import gcd


# ==========================================
# 1. VALIDAR CONVERSION DE MIXTA A IMPROPIA
# ==========================================

def validar_mixta_a_impropia(
    entero,
    numerador,
    denominador,
    numerador_estudiante,
    denominador_estudiante
):
    """
    Comprueba la conversion de un numero mixto
    a una fraccion impropia.
    """

    if entero < 0 or numerador < 0 or denominador <= 0:
        return {
            "valido": False,
            "mensaje": "Los valores ingresados no son validos."
        }

    if numerador >= denominador:
        return {
            "valido": False,
            "mensaje": "La parte fraccionaria debe ser propia."
        }

    numerador_correcto = (
        entero * denominador + numerador
    )

    if (
        numerador_estudiante == numerador_correcto
        and denominador_estudiante == denominador
    ):
        return {
            "valido": True,
            "mensaje": "La conversion a fraccion impropia es correcta."
        }

    return {
        "valido": False,
        "mensaje": (
            "Recuerda multiplicar el entero por el denominador "
            "y sumar el numerador."
        )
    }


# ==========================================
# 2. VALIDAR INVERSO DE LA SEGUNDA FRACCION
# ==========================================

def validar_inverso(
    numerador,
    denominador,
    numerador_inverso,
    denominador_inverso
):
    """
    Comprueba que se haya invertido correctamente
    la segunda fraccion de una division.
    """

    if numerador <= 0 or denominador <= 0:
        return {
            "valido": False,
            "mensaje": "La fraccion debe tener valores positivos."
        }

    if (
        numerador_inverso == denominador
        and denominador_inverso == numerador
    ):
        return {
            "valido": True,
            "mensaje": "El inverso de la segunda fraccion es correcto."
        }

    return {
        "valido": False,
        "mensaje": (
            "Debes invertir la segunda fraccion, "
            "intercambiando su numerador y denominador."
        )
    }


# ==========================================
# 3. VALIDAR SIMPLIFICACION CRUZADA
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
    Comprueba la simplificacion cruzada despues
    de convertir la division en multiplicacion.
    """

    if min(
        numerador1, denominador1,
        numerador2, denominador2
    ) <= 0:
        return {
            "valido": False,
            "mensaje": "Los valores deben ser positivos."
        }

    divisor1 = gcd(numerador1, denominador2)
    divisor2 = gcd(numerador2, denominador1)

    n1_correcto = numerador1 // divisor1
    d2_correcto = denominador2 // divisor1

    n2_correcto = numerador2 // divisor2
    d1_correcto = denominador1 // divisor2

    if (
        n1_estudiante == n1_correcto
        and d1_estudiante == d1_correcto
        and n2_estudiante == n2_correcto
        and d2_estudiante == d2_correcto
    ):
        return {
            "valido": True,
            "mensaje": "La simplificacion cruzada es correcta."
        }

    return {
        "valido": False,
        "mensaje": (
            "Revisa la simplificacion entre numeradores "
            "y denominadores opuestos."
        )
    }


# ==========================================
# 4. VALIDAR RESULTADO DE LA DIVISION
# ==========================================

def validar_division(
    numerador1,
    denominador1,
    numerador2,
    denominador2,
    entero_resultado,
    numerador_resultado,
    denominador_resultado
):
    """
    Comprueba el resultado de una division de fracciones.
    Cuando el resultado es impropio, solicita expresarlo
    como numero mixto.
    """

    if denominador1 <= 0 or denominador2 <= 0:
        return {
            "valido": False,
            "mensaje": "Los denominadores deben ser positivos."
        }

    if numerador2 == 0:
        return {
            "valido": False,
            "mensaje": "No se puede dividir entre cero."
        }

    if denominador_resultado <= 0:
        return {
            "valido": False,
            "mensaje": "El denominador del resultado debe ser positivo."
        }

    if min(
        numerador1,
        numerador2,
        entero_resultado,
        numerador_resultado
    ) < 0:
        return {
            "valido": False,
            "mensaje": "Los valores no pueden ser negativos."
        }

    resultado_correcto = (
        Fraction(numerador1, denominador1)
        / Fraction(numerador2, denominador2)
    )

    resultado_estudiante = Fraction(
        entero_resultado * denominador_resultado
        + numerador_resultado,
        denominador_resultado
    )

    if resultado_estudiante != resultado_correcto:
        return {
            "valido": False,
            "mensaje": "El resultado de la division es incorrecto."
        }

    # Si el resultado es impropio, solicitar numero mixto.
    if resultado_correcto >= 1 and numerador_resultado >= denominador_resultado:
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": (
                "El resultado es equivalente, pero debes "
                "convertir la fraccion impropia a numero mixto."
            )
        }

    # Comprobar simplificacion.
    fraccion_original = Fraction(
        numerador_resultado,
        denominador_resultado
    )

    if (
        fraccion_original.numerator != numerador_resultado
        or fraccion_original.denominator != denominador_resultado
    ):
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": "El resultado es correcto, pero falta simplificar."
        }

    return {
        "valido": True,
        "mensaje": "La division es correcta y el resultado esta simplificado."
    }


# ==========================================
# 5. PRUEBAS DEL MODULO
# ==========================================

if __name__ == "__main__":

    print("\n========== D01: CONVERSION DE MIXTA A IMPROPIA ==========")

    print(validar_mixta_a_impropia(
        2, 2, 5,
        12, 5
    ))

    print("\n========== D02: INVERSION DE SEGUNDA FRACCION ==========")

    print(validar_inverso(
        1, 8,
        8, 1
    ))

    print("\n========== D03: SIMPLIFICACION CRUZADA ==========")

    print(validar_simplificacion_cruzada(
        9, 10,
        8, 1,
        9, 5,
        4, 1
    ))

    print("\n========== D04: RESULTADO 7 1/5 ==========")

    print(validar_division(
        9, 10,
        1, 8,
        7, 1, 5
    ))

    print("\n========== D05: SEGUNDA SIMPLIFICACION CRUZADA ==========")

    print(validar_simplificacion_cruzada(
        12, 5,
        15, 8,
        3, 1,
        3, 2
    ))

    print("\n========== D06: RESULTADO 4 1/2 ==========")

    print(validar_division(
        12, 5,
        8, 15,
        4, 1, 2
    ))

    print("\n========== D07: INVERSO INCORRECTO ==========")

    print(validar_inverso(
        1, 8,
        1, 8
    ))

    print("\n========== D08: RESULTADO IMPROPIO ==========")

    print(validar_division(
        9, 10,
        1, 8,
        0, 36, 5
    ))

    print("\n========== D09: DIVISION ENTRE CERO ==========")

    print(validar_division(
        1, 2,
        0, 1,
        0, 0, 1
    ))
