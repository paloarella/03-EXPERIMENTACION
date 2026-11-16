
from math import gcd


def validar_fraccion(numerador, denominador):
    if type(numerador) is not int or type(denominador) is not int:
        raise TypeError("El numerador y el denominador deben ser enteros.")

    if numerador < 0:
        raise ValueError("El numerador no puede ser negativo.")

    if denominador <= 0:
        raise ValueError("El denominador debe ser positivo.")


def convertir_mixta_a_impropia(entero, numerador, denominador):
    """Convierte una fracción mixta positiva en impropia."""

    if any(type(x) is not int for x in (entero, numerador, denominador)):
        raise TypeError("Todos los valores deben ser enteros.")

    if entero < 0 or numerador < 0 or denominador <= 0:
        raise ValueError("Los valores de la fracción no son válidos.")

    if numerador >= denominador:
        raise ValueError(
            "El numerador de la parte fraccionaria debe ser menor "
            "que el denominador."
        )

    nuevo_numerador = entero * denominador + numerador

    return {
        "numerador": nuevo_numerador,
        "denominador": denominador,
        "paso": (
            f"Multiplicar el entero por el denominador y sumar "
            f"el numerador: ({entero} x {denominador} + "
            f"{numerador})/{denominador} = "
            f"{nuevo_numerador}/{denominador}."
        )
    }


def convertir_impropia_a_mixta(numerador, denominador):
    """Convierte una fracción impropia en mixta."""

    validar_fraccion(numerador, denominador)

    entero = numerador // denominador
    residuo = numerador % denominador

    if residuo == 0:
        resultado = str(entero)
    elif entero == 0:
        resultado = f"{residuo}/{denominador}"
    else:
        resultado = f"{entero} {residuo}/{denominador}"

    return {
        "entero": entero,
        "numerador": residuo,
        "denominador": denominador,
        "resultado": resultado
    }


def simplificar_cruzado(n1, d1, n2, d2):
    """Simplifica factores comunes antes de multiplicar."""

    validar_fraccion(n1, d1)
    validar_fraccion(n2, d2)

    divisor1 = gcd(n1, d2)
    divisor2 = gcd(n2, d1)

    nuevo_n1 = n1 // divisor1
    nuevo_d2 = d2 // divisor1

    nuevo_n2 = n2 // divisor2
    nuevo_d1 = d1 // divisor2

    pasos = []

    if divisor1 > 1:
        pasos.append(
            f"Dividir {n1} y {d2} entre {divisor1}."
        )

    if divisor2 > 1:
        pasos.append(
            f"Dividir {n2} y {d1} entre {divisor2}."
        )

    return {
        "numerador1": nuevo_n1,
        "denominador1": nuevo_d1,
        "numerador2": nuevo_n2,
        "denominador2": nuevo_d2,
        "pasos": pasos
    }


def multiplicar_fracciones(n1, d1, n2, d2):
    """Multiplica dos fracciones aplicando simplificación cruzada."""

    simplificacion = simplificar_cruzado(n1, d1, n2, d2)

    resultado_numerador = (
        simplificacion["numerador1"] *
        simplificacion["numerador2"]
    )

    resultado_denominador = (
        simplificacion["denominador1"] *
        simplificacion["denominador2"]
    )

    return {
        "simplificacion": simplificacion,
        "resultado_numerador": resultado_numerador,
        "resultado_denominador": resultado_denominador
    }


if __name__ == "__main__":

    print("===== PRUEBA 1: FRACCIÓN MIXTA A IMPROPIA =====")

    mixta = convertir_mixta_a_impropia(2, 2, 5)
    print(mixta["paso"])

    print("\n===== PRUEBA 2: SIMPLIFICACIÓN CRUZADA =====")

    simplificada = simplificar_cruzado(12, 5, 15, 8)

    for paso in simplificada["pasos"]:
        print(paso)

    print(
        "Fracciones resultantes:",
        f'{simplificada["numerador1"]}/'
        f'{simplificada["denominador1"]} x '
        f'{simplificada["numerador2"]}/'
        f'{simplificada["denominador2"]}'
    )

    print("\n===== PRUEBA 3: MULTIPLICACIÓN =====")

    producto = multiplicar_fracciones(3, 1, 3, 2)

    print(
        "Resultado:",
        f'{producto["resultado_numerador"]}/'
        f'{producto["resultado_denominador"]}'
    )

    print("\n===== PRUEBA 4: IMPROPIA A MIXTA =====")

    mixta_final = convertir_impropia_a_mixta(9, 2)
    print("Resultado:", mixta_final["resultado"])
