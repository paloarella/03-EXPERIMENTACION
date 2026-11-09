
# ==========================================
# MODULO DE CALCULO Y VALIDACION DEL MCM
# ==========================================

def calcular_mcm(a, b):
    """
    Calcula el minimo comun multiplo
    de dos numeros enteros positivos.
    """

    if a <= 0 or b <= 0:
        raise ValueError(
            "Los numeros deben ser enteros positivos."
        )

    mayor = max(a, b)

    while True:
        if mayor % a == 0 and mayor % b == 0:
            return mayor

        mayor += 1


def validar_mcm(a, b, mcm_estudiante):
    """
    Comprueba si el MCM indicado por el estudiante
    corresponde al minimo comun multiplo real.
    """

    mcm_correcto = calcular_mcm(a, b)

    if mcm_estudiante == mcm_correcto:
        return {
            "valido": True,
            "mcm_correcto": mcm_correcto,
            "mensaje": "El MCM es correcto."
        }

    elif (
        mcm_estudiante > 0
        and mcm_estudiante % a == 0
        and mcm_estudiante % b == 0
    ):
        return {
            "valido": False,
            "mcm_correcto": mcm_correcto,
            "mensaje": (
                "El numero es un multiplo comun, "
                "pero no es el minimo comun multiplo."
            )
        }

    else:
        return {
            "valido": False,
            "mcm_correcto": mcm_correcto,
            "mensaje": (
                "El numero indicado no es un "
                "multiplo comun de ambos denominadores."
            )
        }


# ==========================================
# PRUEBAS INICIALES DEL MODULO
# ==========================================

if __name__ == "__main__":

    pruebas = [
        (5, 6, 30),
        (15, 20, 60),
        (15, 30, 30),
        (15, 20, 120),
        (15, 30, 15),
        (2, 8, 8)
    ]

    for a, b, respuesta in pruebas:

        print("\n------------------------------")
        print(f"Denominadores: {a} y {b}")
        print(f"MCM indicado: {respuesta}")

        resultado = validar_mcm(a, b, respuesta)

        print("Resultado:", resultado)
