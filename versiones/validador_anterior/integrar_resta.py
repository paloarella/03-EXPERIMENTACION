
from resta import (
    validar_mcm_resta,
    validar_conversion_fracciones,
    validar_conversion_entero,
    validar_prestamo,
    validar_resta
)


def integrar_resta(datos):
    """Valida los pasos de una resta de fracciones."""

    try:
        # 1. Validar MCM
        resultado = validar_mcm_resta(
            datos["denominador1"],
            datos["denominador2"],
            datos["mcm_estudiante"]
        )

        if not resultado.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 1,
                "mensaje": resultado.get("mensaje")
            }

        # 2. Validar conversiones de fracciones
        resultado = validar_conversion_fracciones(
            datos["numerador1"],
            datos["denominador1"],
            datos["numerador2"],
            datos["denominador2"],
            datos["mcm_estudiante"],
            datos["n1_equivalente"],
            datos["d1_equivalente"],
            datos["n2_equivalente"],
            datos["d2_equivalente"]
        )

        if not resultado.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 2,
                "mensaje": resultado.get("mensaje")
            }

        # 3. Validar conversión de enteros, si aplica
        if datos["entero1"] > 0:
            resultado = validar_conversion_entero(
                datos["entero1"],
                datos["mcm_estudiante"],
                datos["numerador_entero"],
                datos["denominador_entero"]
            )

            if not resultado.get("valido"):
                return {
                    "estado": "incorrecto",
                    "paso": 3,
                    "mensaje": resultado.get("mensaje")
                }

        
        # 4. Determinar si matemáticamente se necesita préstamo
        necesita_prestamo = (
            datos["n1_equivalente"] < datos["n2_equivalente"]
        )

        solicita_prestamo = datos.get("requiere_prestamo", False)

        if necesita_prestamo:

            if datos["entero1"] <= 0:
                return {
                    "estado": "incorrecto",
                    "paso": 4,
                    "mensaje": (
                        "La resta produce un resultado negativo "
                        "o requiere un caso fuera del alcance."
                    )
                }

            if not solicita_prestamo:
                return {
                    "estado": "incorrecto",
                    "paso": 4,
                    "mensaje": (
                        "La parte fraccionaria del minuendo es menor "
                        "que la del sustraendo. Debes realizar un préstamo."
                    )
                }

            resultado = validar_prestamo(
                datos["entero1"],
                datos["n1_equivalente"],
                datos["mcm_estudiante"],
                datos["n2_equivalente"],
                datos["entero_prestamo"],
                datos["numerador_prestamo"],
                datos["denominador_prestamo"]
            )

            if not resultado.get("valido"):
                return {
                    "estado": "incorrecto",
                    "paso": 4,
                    "mensaje": resultado.get("mensaje")
                }

        elif solicita_prestamo:
            return {
                "estado": "incorrecto",
                "paso": 4,
                "mensaje": (
                    "En este caso no se necesita realizar un préstamo."
                )
            }

        # 5. Validar resultado de la resta
        resultado = validar_resta(
            datos["entero1"],
            datos["n1_equivalente"],
            datos["mcm_estudiante"],
            datos["entero2"],
            datos["n2_equivalente"],
            datos["mcm_estudiante"],
            datos["entero_resultado"],
            datos["numerador_resultado"],
            datos["denominador_resultado"]
        )

        if not resultado.get("valido"):
            return {
                "estado": (
                    "incompleto"
                    if resultado.get("incompleto")
                    else "incorrecto"
                ),
                "paso": 5,
                "mensaje": resultado.get("mensaje")
            }

        return {
            "estado": "correcto",
            "mensaje": "¡Muy bien! Todos los pasos de la resta son correctos."
        }

    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        return {
            "estado": "error",
            "mensaje": f"No se pudo validar el procedimiento: {error}"
        }


if __name__ == "__main__":

    # Ejemplo: 1 2/9 - 4/9 = 7/9
    datos = {
        "entero1": 1,
        "numerador1": 2,
        "denominador1": 9,
        "entero2": 0,
        "numerador2": 4,
        "denominador2": 9,

        "mcm_estudiante": 9,

        "n1_equivalente": 2,
        "d1_equivalente": 9,
        "n2_equivalente": 4,
        "d2_equivalente": 9,

        "numerador_entero": 9,
        "denominador_entero": 9,

        "requiere_prestamo": True,
        "entero_prestamo": 0,
        "numerador_prestamo": 11,
        "denominador_prestamo": 9,

        "entero_resultado": 0,
        "numerador_resultado": 7,
        "denominador_resultado": 9
    }

    print("========== INTEGRACIÓN DE RESTA ==========")
    print(integrar_resta(datos))
