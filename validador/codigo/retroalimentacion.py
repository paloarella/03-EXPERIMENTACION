
def generar_retroalimentacion(resultado):
    """
    Genera un mensaje de retroalimentación a partir
    del resultado de una validación.
    """

    if resultado.get("valido"):
        return {
            "estado": "correcto",
            "mensaje": "¡Muy bien! El procedimiento es correcto."
        }

    if resultado.get("incompleto"):
        return {
            "estado": "incompleto",
            "mensaje": resultado.get(
                "mensaje",
                "Tu procedimiento está incompleto. Revisa los pasos."
            )
        }

    return {
        "estado": "incorrecto",
        "mensaje": resultado.get(
            "mensaje",
            "Hay un error en tu procedimiento. Revisa el paso señalado."
        )
    }


# Pruebas
if __name__ == "__main__":

    casos = [
        {
            "nombre": "Caso 1: procedimiento correcto",
            "resultado": {
                "valido": True
            }
        },
        {
            "nombre": "Caso 2: procedimiento incorrecto",
            "resultado": {
                "valido": False,
                "mensaje": "El resultado de la resta no coincide."
            }
        },
        {
            "nombre": "Caso 3: procedimiento incompleto",
            "resultado": {
                "valido": False,
                "incompleto": True,
                "mensaje": "Convierte la fracción impropia a número mixto."
            }
        }
    ]

    for caso in casos:
        print("\n" + caso["nombre"])
        print(generar_retroalimentacion(caso["resultado"]))
