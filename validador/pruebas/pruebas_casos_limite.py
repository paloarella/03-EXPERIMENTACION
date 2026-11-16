from validador.codigo.motor_matematico import operar_fracciones

def ejecutar_prueba(nombre, funcion):
    print(f"\n========== {nombre} ==========")
    try:
        resultado = funcion()
        print("Resultado:", resultado)
    except Exception as error:
        print("Excepción:", type(error).__name__)
        print("Mensaje:", error)

# 1. Resultado cero
ejecutar_prueba(
    "RESULTADO CERO",
    lambda: operar_fracciones(1, 2, 1, 2, "-")
)

# 2. Suma con cero
ejecutar_prueba(
    "SUMA CON CERO",
    lambda: operar_fracciones(1, 3, 0, 5, "+")
)

# 3. Resultado entero
ejecutar_prueba(
    "RESULTADO ENTERO",
    lambda: operar_fracciones(1, 2, 1, 2, "+")
)

# 4. División entre cero
ejecutar_prueba(
    "DIVISIÓN ENTRE CERO",
    lambda: operar_fracciones(1, 2, 0, 3, "/")
)

# 5. Resta con resultado negativo
ejecutar_prueba(
    "RESTA NEGATIVA",
    lambda: operar_fracciones(1, 4, 3, 4, "-")
)

# 6. Denominador cero
ejecutar_prueba(
    "DENOMINADOR CERO",
    lambda: operar_fracciones(1, 0, 1, 2, "+")
)

# 7. Operador no válido
ejecutar_prueba(
    "OPERADOR NO VÁLIDO",
    lambda: operar_fracciones(1, 2, 1, 3, "%")
)
