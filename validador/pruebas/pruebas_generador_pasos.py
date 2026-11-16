from validador.codigo.motor_matematico import operar_fracciones
from validador.codigo.generador_pasos import generar_explicacion

def probar_generador():
    casos = [
        ("Suma", 2, 3, 1, 4, "+"),
        ("Resta", 7, 8, 1, 4, "-"),
        ("Multiplicación", 2, 3, 3, 4, "*"),
        ("División", 2, 3, 4, 5, "/")
    ]

    for nombre, n1, d1, n2, d2, operador in casos:

        resultado_motor = operar_fracciones(
            n1, d1, n2, d2, operador
        )

        explicacion = generar_explicacion(resultado_motor)

        assert len(explicacion["explicacion"]) > 0
        assert explicacion["resultado"] == resultado_motor["resultado"]

        print(f"[APROBADA] {nombre}")
        print("Resultado:", explicacion["resultado"]["mixto"])
        print("Pasos generados:", len(explicacion["explicacion"]))

if __name__ == "__main__":
    probar_generador()
    print("\nTodas las pruebas del generador finalizaron correctamente.")