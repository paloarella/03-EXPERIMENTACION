
from fractions import Fraction

from division import (
    validar_mixta_a_impropia,
    validar_inverso,
    validar_simplificacion_cruzada,
    validar_division
)


def integrar_division(datos):
    """Valida los pasos de una division de fracciones."""

    try:
        n1 = datos["numerador1"]
        d1 = datos["denominador1"]

        # 1. Conversion de numero mixto a fraccion impropia
        if datos.get("es_mixto", False):
            resultado = validar_mixta_a_impropia(
                datos["entero1"],
                n1,
                d1,
                datos["numerador_impropio"],
                datos["denominador_impropio"]
            )

            if not resultado.get("valido"):
                return {
                    "estado": "incorrecto",
                    "paso": 1,
                    "mensaje": resultado.get("mensaje")
                }

            n1 = datos["numerador_impropio"]
            d1 = datos["denominador_impropio"]

        # 2. Inversion de la segunda fraccion
        n2 = datos["numerador2"]
        d2 = datos["denominador2"]

        resultado = validar_inverso(
            n2,
            d2,
            datos["numerador_inverso"],
            datos["denominador_inverso"]
        )

        if not resultado.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 2,
                "mensaje": resultado.get("mensaje")
            }

        ni = datos["numerador_inverso"]
        di = datos["denominador_inverso"]

        # 3. Simplificacion cruzada
        resultado = validar_simplificacion_cruzada(
            n1, d1,
            ni, di,
            datos["n1_cruzado"],
            datos["d1_cruzado"],
            datos["n2_cruzado"],
            datos["d2_cruzado"]
        )

        if not resultado.get("valido"):
            return {
                "estado": "incorrecto",
                "paso": 3,
                "mensaje": resultado.get("mensaje")
            }

        # 4. Multiplicacion de las fracciones simplificadas
        producto_correcto = Fraction(n1, d1) / Fraction(n2, d2)

        producto_estudiante = (
            Fraction(datos["n1_cruzado"], datos["d1_cruzado"])
            * Fraction(datos["n2_cruzado"], datos["d2_cruzado"])
        )

        if producto_estudiante != producto_correcto:
            return {
                "estado": "incorrecto",
                "paso": 4,
                "mensaje": (
                    "Revisa la multiplicacion de las fracciones "
                    "despues de la simplificacion cruzada."
                )
            }

        # 5. Resultado final
        resultado = validar_division(
            n1,
            d1,
            n2,
            d2,
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
            "mensaje": (
                "¡Muy bien! Todos los pasos de la division "
                "son correctos."
            )
        }

    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        return {
            "estado": "error",
            "mensaje": f"No se pudo validar el procedimiento: {error}"
        }


if __name__ == "__main__":

    datos = {
        "es_mixto": True,
        "entero1": 2,
        "numerador1": 2,
        "denominador1": 5,

        "numerador_impropio": 12,
        "denominador_impropio": 5,

        "numerador2": 8,
        "denominador2": 15,

        "numerador_inverso": 15,
        "denominador_inverso": 8,

        "n1_cruzado": 3,
        "d1_cruzado": 1,
        "n2_cruzado": 3,
        "d2_cruzado": 2,

        "entero_resultado": 4,
        "numerador_resultado": 1,
        "denominador_resultado": 2
    }

    print("========== INTEGRACION DE DIVISION ==========")
    print(integrar_division(datos))
