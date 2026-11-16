
from fractions import Fraction
from mcm import calcular_mcm


def mostrar_fraccion(numerador, denominador):
    """Devuelve una fracción en formato legible."""
    if denominador == 1:
        return str(numerador)

    return f"{numerador}/{denominador}"


def generar_suma(n1, d1, n2, d2):
    """
    Resuelve una suma de fracciones y genera
    una explicación ordenada de sus pasos.
    """

    # Validación de los datos de entrada.
    if not all(isinstance(x, int) for x in (n1, d1, n2, d2)):
        raise TypeError("Los valores deben ser números enteros.")

    if d1 <= 0 or d2 <= 0:
        raise ValueError("Los denominadores deben ser positivos.")

    if n1 < 0 or n2 < 0:
        raise ValueError("Los numeradores no pueden ser negativos.")

    # Cálculo del mínimo común múltiplo.
    mcm = calcular_mcm(d1, d2)

    # Conversión a fracciones equivalentes.
    factor1 = mcm // d1
    factor2 = mcm // d2

    nuevo_n1 = n1 * factor1
    nuevo_n2 = n2 * factor2

    # Suma de numeradores.
    suma_numeradores = nuevo_n1 + nuevo_n2

    # Simplificación exacta del resultado.
    resultado = Fraction(suma_numeradores, mcm)

    # Construcción de los pasos explicativos.
    pasos = [
        f"1. Identificar la operación: suma de {n1}/{d1} y {n2}/{d2}.",
        f"2. Calcular el mínimo común múltiplo de {d1} y {d2}: {mcm}.",
        (
            f"3. Convertir las fracciones a denominador común: "
            f"{n1}/{d1} = {nuevo_n1}/{mcm} y "
            f"{n2}/{d2} = {nuevo_n2}/{mcm}."
        ),
        (
            f"4. Sumar los numeradores y conservar el denominador: "
            f"({nuevo_n1} + {nuevo_n2})/{mcm} = "
            f"{suma_numeradores}/{mcm}."
        )
    ]

    if resultado.numerator != suma_numeradores or resultado.denominator != mcm:
        pasos.append(
            f"5. Simplificar la fracción: "
            f"{suma_numeradores}/{mcm} = "
            f"{mostrar_fraccion(resultado.numerator, resultado.denominator)}."
        )
    else:
        pasos.append("5. La fracción ya se encuentra simplificada.")

    return {
        "operacion": "suma",
        "pasos": pasos,
        "resultado_numerador": resultado.numerator,
        "resultado_denominador": resultado.denominator,
        "resultado": mostrar_fraccion(
            resultado.numerator,
            resultado.denominator
        )
    }


if __name__ == "__main__":
    solucion = generar_suma(2, 3, 1, 4)

    print("========== GENERADOR DE SUMAS ==========")

    for paso in solucion["pasos"]:
        print(paso)

    print("\nResultado final:", solucion["resultado"])
