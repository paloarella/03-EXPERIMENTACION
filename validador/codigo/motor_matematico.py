
from math import gcd


# ==========================================
# 1. VALIDACIÓN DE ENTRADAS
# ==========================================

def validar_entrada(n1, d1, n2, d2, operacion):

    valores = (n1, d1, n2, d2)

    if any(type(valor) is not int for valor in valores):
        raise TypeError("Los numeradores y denominadores deben ser enteros.")

    if d1 == 0 or d2 == 0:
        raise ValueError("Los denominadores no pueden ser cero.")

    if operacion not in ("+", "-", "*", "/"):
        raise ValueError("Operación no válida.")

    if operacion == "/" and n2 == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")


# ==========================================
# 2. NORMALIZACIÓN Y SIMPLIFICACIÓN
# ==========================================

def normalizar(numerador, denominador):
    """
    Mantiene el denominador positivo y reduce
    la fracción a su forma irreducible.
    """

    if denominador == 0:
        raise ZeroDivisionError("El denominador no puede ser cero.")

    if denominador < 0:
        numerador = -numerador
        denominador = -denominador

    divisor = gcd(abs(numerador), denominador)

    return numerador // divisor, denominador // divisor


def calcular_mcm(a, b):
    """Calcula el mínimo común múltiplo."""

    return abs(a * b) // gcd(a, b)


# ==========================================
# 3. REPRESENTACIÓN DEL RESULTADO
# ==========================================

def generar_resultado(numerador, denominador):

    n, d = normalizar(numerador, denominador)

    if n == 0:
        mixto = "0"

    elif abs(n) >= d:

        entero = abs(n) // d
        residuo = abs(n) % d

        signo = "-" if n < 0 else ""

        if residuo == 0:
            mixto = f"{signo}{entero}"
        else:
            mixto = f"{signo}{entero} {residuo}/{d}"

    else:
        mixto = f"{n}/{d}"

    return {
        "numerador": n,
        "denominador": d,
        "fraccion": f"{n}/{d}",
        "mixto": mixto
    }


# ==========================================
# 4. REGISTRO DE PASOS
# ==========================================

def agregar_paso(pasos, regla, descripcion, expresion=None):

    pasos.append({
        "regla": regla,
        "descripcion": descripcion,
        "expresion": expresion
    })


# ==========================================
# 5. MOTOR GENERAL
# ==========================================

def operar_fracciones(n1, d1, n2, d2, operacion):

    validar_entrada(n1, d1, n2, d2, operacion)

    pasos = []

    expresion = f"{n1}/{d1} {operacion} {n2}/{d2}"

    agregar_paso(
        pasos,
        "R00",
        "Identificar la operación y sus dos fracciones.",
        expresion
    )

    # --------------------------------------
    # SUMA Y RESTA
    # --------------------------------------

    if operacion in ("+", "-"):

        mcm = calcular_mcm(d1, d2)

        agregar_paso(
            pasos,
            "R01",
            f"Calcular el denominador común: MCM({d1}, {d2}) = {mcm}."
        )

        factor1 = mcm // d1
        factor2 = mcm // d2

        nuevo_n1 = n1 * factor1
        nuevo_n2 = n2 * factor2

        agregar_paso(
            pasos,
            "R02",
            "Convertir las fracciones a denominadores iguales.",
            f"{nuevo_n1}/{mcm} {operacion} {nuevo_n2}/{mcm}"
        )

        if operacion == "+":
            numerador = nuevo_n1 + nuevo_n2
            nombre = "sumar"

        else:
            numerador = nuevo_n1 - nuevo_n2
            nombre = "restar"

        denominador = mcm

        agregar_paso(
            pasos,
            "R03",
            f"Conservar el denominador y {nombre} los numeradores.",
            f"{nuevo_n1} {operacion} {nuevo_n2} = {numerador}"
        )

    # --------------------------------------
    # MULTIPLICACIÓN
    # --------------------------------------

    elif operacion == "*":

        numerador = n1 * n2
        denominador = d1 * d2

        agregar_paso(
            pasos,
            "R04",
            "Multiplicar los numeradores entre sí.",
            f"{n1} × {n2} = {numerador}"
        )

        agregar_paso(
            pasos,
            "R05",
            "Multiplicar los denominadores entre sí.",
            f"{d1} × {d2} = {denominador}"
        )

    # --------------------------------------
    # DIVISIÓN
    # --------------------------------------

    else:

        agregar_paso(
            pasos,
            "R06",
            "Invertir la segunda fracción y convertir "
            "la división en multiplicación.",
            f"{n1}/{d1} × {d2}/{n2}"
        )

        numerador = n1 * d2
        denominador = d1 * n2

        agregar_paso(
            pasos,
            "R04",
            "Multiplicar los numeradores.",
            f"{n1} × {d2} = {numerador}"
        )

        agregar_paso(
            pasos,
            "R05",
            "Multiplicar los denominadores.",
            f"{d1} × {n2} = {denominador}"
        )

    # --------------------------------------
    # SIMPLIFICACIÓN
    # --------------------------------------

    resultado = generar_resultado(numerador, denominador)

    if (
        resultado["numerador"] != numerador
        or resultado["denominador"] != denominador
    ):

        agregar_paso(
            pasos,
            "R07",
            "Simplificar la fracción dividiendo "
            "el numerador y el denominador por su MCD.",
            resultado["fraccion"]
        )

    else:

        agregar_paso(
            pasos,
            "R08",
            "La fracción obtenida ya está simplificada.",
            resultado["fraccion"]
        )

    agregar_paso(
        pasos,
        "R09",
        "Presentar el resultado final.",
        resultado["mixto"]
    )

    return {
        "entrada": {
            "numerador1": n1,
            "denominador1": d1,
            "numerador2": n2,
            "denominador2": d2,
            "operacion": operacion
        },
        "pasos": pasos,
        "resultado": resultado
    }


# ==========================================
# 6. PRUEBAS DE EJEMPLO
# ==========================================

if __name__ == "__main__":

    pruebas = [
        ("Suma", 2, 3, 1, 4, "+"),
        ("Resta", 1, 4, 3, 4, "-"),
        ("Multiplicación", 2, 3, 3, 4, "*"),
        ("División", 2, 3, 4, 5, "/"),
        ("Resultado cero", 1, 2, 1, 2, "-"),
        ("Numeradores negativos", -2, 3, 1, 4, "+"),
        ("Denominadores negativos", 2, -3, 1, 4, "+"),
    ]

    for nombre, n1, d1, n2, d2, operador in pruebas:

        print(f"\n========== {nombre.upper()} ==========")

        resultado = operar_fracciones(
            n1, d1, n2, d2, operador
        )

        for paso in resultado["pasos"]:
            print(
                paso["regla"],
                paso["descripcion"],
                paso["expresion"]
            )

        print("Resultado:", resultado["resultado"])
