from fractions import Fraction
from .mcm import calcular_mcm
from hypothesis import assume

# ==========================================
# 1. VALIDAR EL MCM
# ==========================================

def validar_mcm_resta(d1, d2, mcm_estudiante):
    mcm_correcto = calcular_mcm(d1, d2)

    if mcm_estudiante == mcm_correcto:
        return {
            "valido": True,
            "mensaje": "El MCM es correcto."
        }

    if (
        mcm_estudiante > 0
        and mcm_estudiante % d1 == 0
        and mcm_estudiante % d2 == 0
    ):
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": "Es un multiplo comun, pero no es el minimo."
        }

    return {
        "valido": False,
        "mensaje": "El MCM indicado es incorrecto."
    }


# ==========================================
# 2. VALIDAR CONVERSION DE FRACCIONES
# ==========================================
def validar_conversion_fracciones(
    n1, d1,
    n2, d2,
    mcm_estudiante,
    n1_estudiante, d1_estudiante,
    n2_estudiante, d2_estudiante
):

    if d1 <= 0 or d2 <= 0:
        return {
            "valido": False,
            "mensaje": "Los denominadores deben ser positivos."
        }

    resultado_mcm = validar_mcm_resta(
        d1, d2, mcm_estudiante
    )

    if not resultado_mcm["valido"]:
        return resultado_mcm

    n1_correcto = n1 * (mcm_estudiante // d1)
    n2_correcto = n2 * (mcm_estudiante // d2)

    if (
        n1_estudiante == n1_correcto
        and d1_estudiante == mcm_estudiante
        and n2_estudiante == n2_correcto
        and d2_estudiante == mcm_estudiante
    ):
        return {
            "valido": True,
            "mensaje": "Las conversiones son correctas."
        }

    return {
        "valido": False,
        "mensaje": "Revisa la conversion de las fracciones equivalentes."
    }


# ==========================================
# 3. VALIDAR CONVERSION DE ENTERO
# ==========================================
def validar_conversion_entero(
    entero,
    denominador,
    numerador_estudiante,
    denominador_estudiante
):

    if entero < 0 or denominador <= 0:
        return {
            "valido": False,
            "mensaje": "Los valores ingresados no son validos."
        }
    numerador_correcto = entero * denominador

    if (
        numerador_estudiante == numerador_correcto
        and denominador_estudiante == denominador
    ):
        return {
            "valido": True,
            "mensaje": "La conversion del entero es correcta."
        }

    return {
        "valido": False,
        "mensaje": "Revisa la conversion del entero a fraccion."
    }


# ==========================================
# 4. VALIDAR PRESTAMO DE UNA UNIDAD
# ==========================================
def validar_prestamo(
    entero,
    numerador,
    denominador,
    numerador_sustraendo,
    entero_estudiante,
    numerador_estudiante,
    denominador_estudiante
):

    if denominador <= 0:
        return {
            "valido": False,
            "mensaje": "El denominador debe ser positivo."
        }

    if numerador >= denominador:
        return {
            "valido": False,
            "mensaje": "La fraccion inicial no es propia."
        }

    if numerador >= numerador_sustraendo:
        return {
            "valido": False,
            "mensaje": "En este caso no se necesita realizar un prestamo."
        }

    if entero <= 0:
        return {
            "valido": False,
            "mensaje": "No hay una unidad entera disponible para prestar."
        }

    entero_correcto = entero - 1
    numerador_correcto = denominador + numerador

    if (
        entero_estudiante == entero_correcto
        and numerador_estudiante == numerador_correcto
        and denominador_estudiante == denominador
    ):
        return {
            "valido": True,
            "mensaje": "El prestamo de una unidad es correcto."
        }

    return {
        "valido": False,
        "mensaje": (
            "Debes convertir una unidad entera en una "
            "fraccion equivalente antes de restar."
        )
    }


# ==========================================
# 5. VALIDAR RESULTADO DE LA RESTA
# ==========================================
def validar_resta(
    entero1, numerador1, denominador1,
    entero2, numerador2, denominador2,
    entero_resultado, numerador_resultado,
    denominador_resultado
):

    if denominador1 <= 0 or denominador2 <= 0:
        return {
            "valido": False,
            "mensaje": "Los denominadores deben ser positivos."
        }

    if denominador_resultado <= 0:
        return {
            "valido": False,
            "mensaje": "El denominador del resultado debe ser positivo."
        }

    if min(
        entero1, entero2,
        numerador1, numerador2,
        numerador_resultado
    ) < 0:
        return {
            "valido": False,
            "mensaje": "Los valores no pueden ser negativos en esta prueba."
        }

    valor1 = Fraction(
        entero1 * denominador1 + numerador1,
        denominador1
    )

    valor2 = Fraction(
        entero2 * denominador2 + numerador2,
        denominador2
    )
    resultado_correcto = valor1 - valor2

    resultado_estudiante = Fraction(
        entero_resultado * denominador_resultado
        + numerador_resultado,
        denominador_resultado
    )

    if resultado_correcto < 0:
        return {
            "valido": False,
            "fuera_de_alcance": True,
            "mensaje": "El resultado negativo no forma parte de los casos evaluados."
        }

    if resultado_estudiante != resultado_correcto:
        return {
            "valido": False,
            "mensaje": "El resultado de la resta es incorrecto."
        }

    if numerador_resultado >= denominador_resultado:
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": "Debes expresar correctamente el resultado como numero mixto."
        }

    fraccion_simplificada = Fraction(
        numerador_resultado,
        denominador_resultado
    )

    if (
        fraccion_simplificada.numerator != numerador_resultado
        or fraccion_simplificada.denominator != denominador_resultado
    ):
        return {
            "valido": False,
            "incompleto": True,
            "mensaje": "El resultado es correcto, pero falta simplificar."
        }

    return {
        "valido": True,
        "mensaje": "La resta es correcta y esta simplificada."
    }


# ==========================================
# 6. PRUEBAS DEL MODULO
# ==========================================
if __name__ == "__main__":
    print("\n========== R01: MCM ==========")
    print(validar_mcm_resta(2, 8, 8))

    print("\n========== R02: CONVERSION DE FRACCIONES ==========")
    print(validar_conversion_fracciones(
        1, 2,
        7, 8,
        8,
        4, 8,
        7, 8
    ))

    print("\n========== R03: CONVERSION DE ENTERO ==========")
    print(validar_conversion_entero(1, 11, 11, 11))

    print("\n========== R04: PRESTAMO CORRECTO ==========")
    print(validar_prestamo(
        1, 2, 9,
        4,
        0, 11, 9
    ))

    print("\n========== R05: RESULTADO DE RESTA ==========")
    print(validar_resta(
        1, 2, 9,
        0, 4, 9,
        0, 7, 9
    ))

    print("\n========== R06: RESTA DE MIXTOS ==========")
    print(validar_resta(
        3, 1, 2,
        1, 7, 8,
        1, 5, 8
    ))

    print("\n========== R07: PRESTAMO INCORRECTO ==========")
    print(validar_prestamo(
        3, 4, 8,
        7,
        3, 4, 8
    ))

    print("\n========== R08: RESULTADO SIN SIMPLIFICAR ==========")
    print(validar_resta(
        1, 2, 9,
        0, 4, 9,
        0, 14, 18
    ))

    print("\n========== R09: MCM INCORRECTO ==========")
    print(validar_mcm_resta(2, 8, 16))
