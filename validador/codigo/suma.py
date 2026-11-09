
from fractions import Fraction
from mcm import calcular_mcm


# ==========================================
# 1. VALIDAR CONVERSION A DENOMINADOR COMUN
# ==========================================

def validar_conversion(
    numerador1,
    denominador1,
    numerador2,
    denominador2,
    mcm_estudiante,
    numerador1_estudiante,
    denominador1_estudiante,
    numerador2_estudiante,
    denominador2_estudiante
):
    """
    Comprueba el MCM y la conversion de ambas
    fracciones a un denominador comun.
    """

    if denominador1 <= 0 or denominador2 <= 0:
        raise ValueError("Los denominadores deben ser positivos.")

    mcm_correcto = calcular_mcm(denominador1, denominador2)

    if mcm_estudiante != mcm_correcto:
        if (
            mcm_estudiante > 0
            and mcm_estudiante % denominador1 == 0
            and mcm_estudiante % denominador2 == 0
        ):
            return {
                "valido": False,
                "mensaje": "El numero indicado es un multiplo comun, pero no es el MCM."
            }

        return {
            "valido": False,
            "mensaje": "El MCM indicado es incorrecto."
        }

    numerador1_correcto = numerador1 * (
        mcm_correcto // denominador1
    )

    numerador2_correcto = numerador2 * (
        mcm_correcto // denominador2
    )

    conversion_correcta = (
        numerador1_estudiante == numerador1_correcto
        and denominador1_estudiante == mcm_correcto
        and numerador2_estudiante == numerador2_correcto
        and denominador2_estudiante == mcm_correcto
    )

    if conversion_correcta:
        return {
            "valido": True,
            "mensaje": "Las conversiones de las fracciones son correctas."
        }

    return {
        "valido": False,
        "mensaje": "Existe un error al convertir las fracciones equivalentes."
    }


# ==========================================
# 2. VALIDAR LA SUMA DE NUMERADORES
# ==========================================

def validar_suma(
    numerador1,
    numerador2,
    denominador_comun,
    resultado_numerador,
    resultado_denominador
):
    """
    Comprueba que la suma de las fracciones
    con denominador comun sea correcta.
    """

    if denominador_comun <= 0 or resultado_denominador <= 0:
        return {
            "valido": False,
            "mensaje": "El denominador debe ser positivo."
        }

    resultado_correcto = Fraction(
        numerador1 + numerador2,
        denominador_comun
    )

    resultado_estudiante = Fraction(
        resultado_numerador,
        resultado_denominador
    )

    if resultado_estudiante == resultado_correcto:
        return {
            "valido": True,
            "mensaje": "La suma es matematicamente correcta."
        }

    return {
        "valido": False,
        "mensaje": "Revisa la suma de los numeradores o el denominador."
    }


# ==========================================
# 3. VALIDAR LA SIMPLIFICACION
# ==========================================

def validar_simplificacion(
    numerador,
    denominador,
    numerador_estudiante,
    denominador_estudiante
):
    """
    Comprueba que la fraccion final sea equivalente
    y que se encuentre completamente simplificada.
    """

    if denominador <= 0 or denominador_estudiante <= 0:
        return {
            "valido": False,
            "mensaje": "El denominador debe ser positivo."
        }

    fraccion_original = Fraction(numerador, denominador)

    fraccion_estudiante = Fraction(
        numerador_estudiante,
        denominador_estudiante
    )

    if fraccion_original != fraccion_estudiante:
        return {
            "valido": False,
            "mensaje": "La fraccion final no es equivalente al resultado."
        }

    if (
        fraccion_estudiante.numerator == numerador_estudiante
        and fraccion_estudiante.denominator == denominador_estudiante
    ):
        return {
            "valido": True,
            "mensaje": "La fraccion es correcta y esta simplificada."
        }

    return {
        "valido": False,
        "incompleto": True,
        "mensaje": "El resultado es equivalente, pero falta simplificar."
    }


# ==========================================
# 4. PRUEBAS INICIALES
# ==========================================

if __name__ == "__main__":

    print("\n========== PRUEBA 1: CONVERSION ==========")

    resultado = validar_conversion(
        4, 15,
        3, 20,
        60,
        16, 60,
        9, 60
    )

    print(resultado)

    print("\n========== PRUEBA 2: SUMA ==========")

    resultado = validar_suma(
        16, 9,
        60,
        25, 60
    )

    print(resultado)

    print("\n========== PRUEBA 3: SIMPLIFICACION ==========")

    resultado = validar_simplificacion(
        25, 60,
        5, 12
    )

    print(resultado)

    print("\n========== PRUEBA 4: SUMA INCORRECTA ==========")

    resultado = validar_suma(
        16, 9,
        60,
        24, 60
    )

    print(resultado)

    print("\n========== PRUEBA 5: SIN SIMPLIFICAR ==========")

    resultado = validar_simplificacion(
        25, 60,
        25, 60
    )

    print(resultado)

    print("\n========== PRUEBA 6: CONVERSION INCORRECTA ==========")

    resultado = validar_conversion(
        4, 15,
        3, 20,
        120,
        32, 120,
        18, 120
    )

    print(resultado)
