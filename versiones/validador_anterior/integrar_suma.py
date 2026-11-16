
from mcm import calcular_mcm
from suma import (
    validar_conversion,
    validar_suma,
    validar_simplificacion
)
from retroalimentacion import generar_retroalimentacion


def integrar_suma(datos):
    """
    Valida los pasos de una suma de fracciones.

    Los datos contienen:
    - Fracciones originales.
    - MCM propuesto.
    - Fracciones equivalentes.
    - Resultado de la suma.
    - Resultado simplificado.
    """

    pasos = []

    try:
        # 1. Validar el MCM
        mcm_correcto = calcular_mcm(
            datos["denominador1"],
            datos["denominador2"]
        )

        if datos["mcm_estudiante"] != mcm_correcto:
            return {
                "estado": "incorrecto",
                "paso": 1,
                "mensaje": (
                    "Revisa el mínimo común múltiplo. "
                    "Debes encontrar el menor número divisible "
                    "entre ambos denominadores."
                )
            }

        pasos.append("MCM correcto")

        # 2. Validar las fracciones equivalentes
        conversion = validar_conversion(
            datos["numerador1"],
            datos["denominador1"],
            datos["numerador2"],
            datos["denominador2"],
            datos["mcm_estudiante"],
            datos["numerador1_equivalente"],
            datos["denominador1_equivalente"],
            datos["numerador2_equivalente"],
            datos["denominador2_equivalente"]
        )

        if not conversion.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 2,
                "mensaje": conversion.get("mensaje")
            }

        pasos.append("Conversiones correctas")

        # 3. Validar la suma
        suma = validar_suma(
            datos["numerador1_equivalente"],
            datos["numerador2_equivalente"],
            datos["mcm_estudiante"],
            datos["resultado_numerador"],
            datos["resultado_denominador"]
        )

        if not suma.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 3,
                "mensaje": suma.get("mensaje")
            }

        pasos.append("Suma correcta")

        # 4. Validar simplificación
        simplificacion = validar_simplificacion(
            datos["resultado_numerador"],
            datos["resultado_denominador"],
            datos["numerador_simplificado"],
            datos["denominador_simplificado"]
        )

        if not simplificacion.get("valido"):
            if simplificacion.get("incompleto"):
                return {
                    "estado": "incompleto",
                    "paso": 4,
                    "mensaje": simplificacion.get("mensaje")
                }

            return {
                "estado": "incorrecto",
                "paso": 4,
                "mensaje": simplificacion.get("mensaje")
            }

        pasos.append("Simplificación correcta")

        return {
            "estado": "correcto",
            "pasos_validados": pasos,
            "mensaje": "¡Muy bien! Todos los pasos de la suma son correctos."
        }

    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        return {
            "estado": "error",
            "mensaje": f"No se pudo validar el procedimiento: {error}"
        }


# Pruebas

if __name__ == "__main__":

    datos_base = {
        "numerador1": 4,
        "denominador1": 15,
        "numerador2": 3,
        "denominador2": 20,
        "mcm_estudiante": 60,
        "numerador1_equivalente": 16,
        "denominador1_equivalente": 60,
        "numerador2_equivalente": 9,
        "denominador2_equivalente": 60,
        "resultado_numerador": 25,
        "resultado_denominador": 60,
        "numerador_simplificado": 5,
        "denominador_simplificado": 12
    }

    casos = [
        ("S01: Procedimiento correcto", {}),
        ("S02: MCM incorrecto", {"mcm_estudiante": 120}),
        ("S03: Conversión incorrecta", {
            "numerador1_equivalente": 15
        }),
        ("S04: Suma incorrecta", {
            "resultado_numerador": 24
        }),
        ("S05: Resultado sin simplificar", {
            "numerador_simplificado": 25,
            "denominador_simplificado": 60
        }),
        ("S06: Simplificación incorrecta", {
            "numerador_simplificado": 6,
            "denominador_simplificado": 12
        })
    ]

    for nombre, cambios in casos:
        datos = datos_base.copy()
        datos.update(cambios)

        print(f"\n========== {nombre} ==========")
        print(integrar_suma(datos))

