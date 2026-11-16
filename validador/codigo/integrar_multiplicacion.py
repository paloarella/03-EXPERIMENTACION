
from multiplicacion import (
    validar_simplificacion_cruzada,
    validar_producto
)


def integrar_multiplicacion(datos):
    """Valida el procedimiento de multiplicación de fracciones."""

    try:
        # 1. Validar simplificación cruzada
        resultado = validar_simplificacion_cruzada(
            datos["numerador1"],
            datos["denominador1"],
            datos["numerador2"],
            datos["denominador2"],
            datos["n1_cruzado"],
            datos["d1_cruzado"],
            datos["n2_cruzado"],
            datos["d2_cruzado"]
        )

        if not resultado.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 1,
                "mensaje": resultado.get("mensaje")
            }

        # 2. Validar producto
        resultado = validar_producto(
            datos["n1_cruzado"],
            datos["d1_cruzado"],
            datos["n2_cruzado"],
            datos["d2_cruzado"],
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
                "paso": 2,
                "mensaje": resultado.get("mensaje")
            }

        return {
            "estado": "correcto",
            "mensaje": (
                "¡Muy bien! La simplificación cruzada "
                "y la multiplicación son correctas."
            )
        }

    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        return {
            "estado": "error",
            "mensaje": f"No se pudo validar el procedimiento: {error}"
        }


if __name__ == "__main__":

    # Ejemplo: 1/5 × 5/6 = 1/6
    datos = {
        "numerador1": 1,
        "denominador1": 5,
        "numerador2": 5,
        "denominador2": 6,

        "n1_cruzado": 1,
        "d1_cruzado": 1,
        "n2_cruzado": 1,
        "d2_cruzado": 6,

        "numerador_resultado": 1,
        "denominador_resultado": 6
    }

    print("========== INTEGRACIÓN DE MULTIPLICACIÓN ==========")
    print(integrar_multiplicacion(datos))
