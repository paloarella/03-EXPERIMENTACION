
from fractions import Fraction

from tecnicas_fracciones import (
    convertir_mixta_a_impropia,
    convertir_impropia_a_mixta,
    simplificar_cruzado,
    multiplicar_fracciones
)


def mostrar(n, d):
    resultado = Fraction(n, d)

    if resultado.denominator == 1:
        return str(resultado.numerator)

    return f"{resultado.numerator}/{resultado.denominator}"


def resolver_multiplicacion_mixta(entero, numerador, denominador, segundo):
    """Multiplica una fracción mixta por un entero."""

    conversion = convertir_mixta_a_impropia(
        entero, numerador, denominador
    )

    n1 = conversion["numerador"]
    d1 = conversion["denominador"]

    n2 = segundo
    d2 = 1

    producto = multiplicar_fracciones(n1, d1, n2, d2)

    resultado = Fraction(
        producto["resultado_numerador"],
        producto["resultado_denominador"]
    )

    pasos = [
        f"Convertir la fracción mixta: {conversion['paso']}",
        f"Expresar el entero como fracción: {segundo}/1.",
        f"Multiplicar: {n1}/{d1} x {n2}/{d2}."
    ]

    pasos.extend(producto["simplificacion"]["pasos"])

    pasos.append(
        f"Multiplicar numeradores y denominadores: "
        f"{producto['resultado_numerador']}/"
        f"{producto['resultado_denominador']}."
    )

    mixta = convertir_impropia_a_mixta(
        resultado.numerator,
        resultado.denominator
    )

    pasos.append(
        f"Convertir a número mixto: {mixta['resultado']}."
    )

    return {
        "operacion": "multiplicacion",
        "pasos": pasos,
        "resultado": resultado,
        "resultado_mixto": mixta["resultado"]
    }


def resolver_division_mixta(entero, numerador, denominador,
                            segundo_n, segundo_d):
    """Divide una fracción mixta entre otra fracción."""

    conversion = convertir_mixta_a_impropia(
        entero, numerador, denominador
    )

    n1 = conversion["numerador"]
    d1 = conversion["denominador"]

    if segundo_n == 0:
        raise ZeroDivisionError(
            "No se puede dividir entre una fracción igual a cero."
        )

    if segundo_d <= 0:
        raise ValueError("El denominador debe ser positivo.")

    pasos = [
        f"Convertir la fracción mixta: {conversion['paso']}",
        f"Expresar la operación: {n1}/{d1} ÷ "
        f"{segundo_n}/{segundo_d}."
    ]

    # Invertir la segunda fracción y cambiar división por multiplicación.
    n2 = segundo_d
    d2 = segundo_n

    pasos.append(
        f"Cambiar la división por multiplicación e invertir "
        f"la segunda fracción: {n1}/{d1} x {n2}/{d2}."
    )

    producto = multiplicar_fracciones(n1, d1, n2, d2)

    pasos.extend(producto["simplificacion"]["pasos"])

    pasos.append(
        f"Multiplicar numeradores y denominadores: "
        f"{producto['resultado_numerador']}/"
        f"{producto['resultado_denominador']}."
    )

    resultado = Fraction(
        producto["resultado_numerador"],
        producto["resultado_denominador"]
    )

    mixta = convertir_impropia_a_mixta(
        resultado.numerator,
        resultado.denominator
    )

    pasos.append(
        f"Convertir a número mixto: {mixta['resultado']}."
    )

    return {
        "operacion": "division",
        "pasos": pasos,
        "resultado": resultado,
        "resultado_mixto": mixta["resultado"]
    }


def ejecutar_pruebas():

    pruebas = [
        {
            "id": "M01",
            "funcion": resolver_multiplicacion_mixta,
            "entrada": (1, 1, 11, 6),
            "esperado": Fraction(72, 11)
        },
        {
            "id": "D01",
            "funcion": resolver_division_mixta,
            "entrada": (2, 2, 5, 8, 15),
            "esperado": Fraction(9, 2)
        }
    ]

    aprobadas = 0

    for prueba in pruebas:
        solucion = prueba["funcion"](*prueba["entrada"])

        print("\n" + "=" * 55)
        print("PRUEBA:", prueba["id"])
        print("OPERACIÓN:", solucion["operacion"])

        for numero, paso in enumerate(solucion["pasos"], 1):
            print(f"{numero}. {paso}")

        print("Resultado:", mostrar(
            solucion["resultado"].numerator,
            solucion["resultado"].denominator
        ))

        print("Resultado mixto:", solucion["resultado_mixto"])

        if solucion["resultado"] == prueba["esperado"]:
            print("PRUEBA APROBADA")
            aprobadas += 1
        else:
            print("PRUEBA NO APROBADA")

    print("\nRESUMEN:", aprobadas, "de", len(pruebas), "pruebas aprobadas.")


if __name__ == "__main__":
    ejecutar_pruebas()
