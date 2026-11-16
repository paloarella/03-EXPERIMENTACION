
from fractions import Fraction
from mcm import calcular_mcm


def validar_entrada(n1, d1, n2, d2):
    """Valida los datos de las dos fracciones."""
    valores = (n1, d1, n2, d2)

    if any(type(x) is not int for x in valores):
        raise TypeError("Los valores deben ser números enteros.")

    if d1 <= 0 or d2 <= 0:
        raise ValueError("Los denominadores deben ser positivos.")

    if n1 < 0 or n2 < 0:
        raise ValueError("Los numeradores no pueden ser negativos.")


def formato(fraccion):
    """Representa una fracción de forma legible."""
    if fraccion.denominator == 1:
        return str(fraccion.numerator)

    return f"{fraccion.numerator}/{fraccion.denominator}"


def generar_suma_mcm(n1, d1, n2, d2):
    """Técnica A: denominador común mediante MCM."""
    validar_entrada(n1, d1, n2, d2)

    mcm = calcular_mcm(d1, d2)

    nuevo_n1 = n1 * (mcm // d1)
    nuevo_n2 = n2 * (mcm // d2)

    suma = nuevo_n1 + nuevo_n2
    resultado = Fraction(suma, mcm)

    pasos = [
        f"Identificar la suma: {n1}/{d1} + {n2}/{d2}.",
        f"Calcular el MCM de {d1} y {d2}: {mcm}.",
        f"Obtener fracciones equivalentes: "
        f"{nuevo_n1}/{mcm} + {nuevo_n2}/{mcm}.",
        f"Sumar numeradores: ({nuevo_n1} + {nuevo_n2})/{mcm} "
        f"= {suma}/{mcm}."
    ]

    if resultado.numerator != suma or resultado.denominator != mcm:
        pasos.append(
            f"Simplificar: {suma}/{mcm} = {formato(resultado)}."
        )
    else:
        pasos.append("La fracción ya está simplificada.")

    return {
        "tecnica": "MCM",
        "pasos": pasos,
        "resultado": resultado
    }


def generar_suma_producto(n1, d1, n2, d2):
    """Técnica B: producto de denominadores."""
    validar_entrada(n1, d1, n2, d2)

    denominador = d1 * d2
    nuevo_n1 = n1 * d2
    nuevo_n2 = n2 * d1

    suma = nuevo_n1 + nuevo_n2
    resultado = Fraction(suma, denominador)

    pasos = [
        f"Identificar la suma: {n1}/{d1} + {n2}/{d2}.",
        f"Multiplicar los denominadores: {d1} x {d2} "
        f"= {denominador}.",
        f"Multiplicar cada numerador por el denominador contrario: "
        f"{nuevo_n1}/{denominador} + {nuevo_n2}/{denominador}.",
        f"Sumar numeradores: ({nuevo_n1} + {nuevo_n2})/"
        f"{denominador} = {suma}/{denominador}."
    ]

    if resultado.numerator != suma or resultado.denominator != denominador:
        pasos.append(
            f"Simplificar: {suma}/{denominador} "
            f"= {formato(resultado)}."
        )
    else:
        pasos.append("La fracción ya está simplificada.")

    return {
        "tecnica": "Producto de denominadores",
        "pasos": pasos,
        "resultado": resultado
    }


def generar_suma_simplificando(n1, d1, n2, d2):
    """Técnica C: simplificar las entradas antes de sumar."""
    validar_entrada(n1, d1, n2, d2)

    fraccion1 = Fraction(n1, d1)
    fraccion2 = Fraction(n2, d2)

    pasos = [
        f"Identificar la suma: {n1}/{d1} + {n2}/{d2}."
    ]

    if fraccion1 != Fraction(n1, d1) or (
        fraccion1.numerator != n1 or fraccion1.denominator != d1
    ):
        pasos.append(
            f"Simplificar la primera fracción: "
            f"{n1}/{d1} = {formato(fraccion1)}."
        )

    if fraccion2.numerator != n2 or fraccion2.denominator != d2:
        pasos.append(
            f"Simplificar la segunda fracción: "
            f"{n2}/{d2} = {formato(fraccion2)}."
        )

    mcm = calcular_mcm(
        fraccion1.denominator,
        fraccion2.denominator
    )

    factor1 = mcm // fraccion1.denominator
    factor2 = mcm // fraccion2.denominator

    nuevo_n1 = fraccion1.numerator * factor1
    nuevo_n2 = fraccion2.numerator * factor2

    suma = nuevo_n1 + nuevo_n2
    resultado = Fraction(suma, mcm)

    pasos.extend([
        f"Calcular el MCM de los denominadores simplificados: {mcm}.",
        f"Obtener fracciones equivalentes: "
        f"{nuevo_n1}/{mcm} + {nuevo_n2}/{mcm}.",
        f"Sumar numeradores: ({nuevo_n1} + {nuevo_n2})/"
        f"{mcm} = {suma}/{mcm}."
    ])

    if resultado.numerator != suma or resultado.denominator != mcm:
        pasos.append(
            f"Simplificar el resultado: {suma}/{mcm} "
            f"= {formato(resultado)}."
        )
    else:
        pasos.append("La fracción ya está simplificada.")

    return {
        "tecnica": "Simplificación previa",
        "pasos": pasos,
        "resultado": resultado
    }


def ejecutar_experimentos():
    pruebas = [
        (2, 3, 1, 4),
        (2, 8, 1, 4),
        (3, 6, 1, 6),
        (1, 5, 2, 5),
        (3, 4, 2, 8),
        (0, 5, 1, 3)
    ]

    tecnicas = [
        generar_suma_mcm,
        generar_suma_producto,
        generar_suma_simplificando
    ]

    for prueba in pruebas:
        print("\n" + "=" * 55)
        print(f"OPERACIÓN: {prueba[0]}/{prueba[1]} + "
              f"{prueba[2]}/{prueba[3]}")

        resultados = []

        for tecnica in tecnicas:
            solucion = tecnica(*prueba)
            resultados.append(solucion["resultado"])

            print(f"\nTÉCNICA: {solucion['tecnica']}")

            for numero, paso in enumerate(solucion["pasos"], 1):
                print(f"{numero}. {paso}")

            print("Resultado:", formato(solucion["resultado"]))

        if not all(r == resultados[0] for r in resultados):
            raise AssertionError(
                "Las técnicas produjeron resultados diferentes."
            )

        print("\nCOMPARACIÓN: Las tres técnicas coinciden.")


if __name__ == "__main__":
    ejecutar_experimentos()
