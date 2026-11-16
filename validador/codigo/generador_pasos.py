def generar_explicacion(resultado_motor):
    """
    Organiza los pasos generados por el motor matemático
    para presentarlos de forma ordenada.
    """
    if not isinstance(resultado_motor, dict):
        raise TypeError("Se esperaba un resultado del motor matemático.")

    if "pasos" not in resultado_motor or "resultado" not in resultado_motor:
        raise ValueError("El resultado del motor está incompleto.")

    pasos_motor = resultado_motor["pasos"]

    if not isinstance(pasos_motor, list):
        raise TypeError("Los pasos deben estar contenidos en una lista.")

    explicacion = []

    for numero, paso in enumerate(pasos_motor, start=1):
        if not isinstance(paso, dict):
            raise ValueError("Se encontró un paso con formato incorrecto.")

        regla = paso.get("regla")
        descripcion = paso.get("descripcion")
        expresion = paso.get("expresion")

        texto = f"{numero}. {descripcion}"

        if expresion:
            texto += f" {expresion}"

        explicacion.append({
            "numero": numero,
            "regla": regla,
            "texto": texto
        })

    return {
        "entrada": resultado_motor.get("entrada"),
        "explicacion": explicacion,
        "resultado": resultado_motor["resultado"]
    }

if __name__ == "__main__":
    from validador.codigo.motor_matematico import operar_fracciones
    operaciones = [
        ("Suma", 2, 3, 1, 4, "+"),
        ("Resta", 7, 8, 1, 4, "-"),
        ("Multiplicación", 2, 3, 3, 4, "*"),
        ("División", 2, 3, 4, 5, "/")
    ]

    for nombre, n1, d1, n2, d2, operador in operaciones:
        motor = operar_fracciones(n1, d1, n2, d2, operador)
        explicacion = generar_explicacion(motor)

        print(f"\n========== {nombre.upper()} ==========")

        for paso in explicacion["explicacion"]:
            print(paso["texto"])

        print("Resultado final:", explicacion["resultado"]["mixto"])
