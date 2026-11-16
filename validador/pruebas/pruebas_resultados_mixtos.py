from fractions import Fraction
from validador.codigo.motor_matematico import operar_fracciones

pruebas = [
    {
        "nombre": "Suma con resultado mixto",
        "entrada": (3, 4, 3, 4, "+"),
        "esperado": Fraction(3, 2),
        "mixto": "1 1/2"
    },
    {
        "nombre": "Resta con resultado entero",
        "entrada": (7, 4, 3, 4, "-"),
        "esperado": Fraction(1, 1),
        "mixto": "1"
    },
    {
        "nombre": "Multiplicación con resultado mixto",
        "entrada": (3, 2, 1, 2, "*"),
        "esperado": Fraction(3, 4),
        "mixto": "3/4"
    },
    {
        "nombre": "División con resultado mixto",
        "entrada": (3, 4, 1, 2, "/"),
        "esperado": Fraction(3, 2),
        "mixto": "1 1/2"
    },
    {
        "nombre": "Multiplicación con resultado entero",
        "entrada": (2, 3, 3, 2, "*"),
        "esperado": Fraction(1, 1),
        "mixto": "1"
    },
]


if __name__ == "__main__":
    aprobadas = 0

    for prueba in pruebas:
        resultado = operar_fracciones(*prueba["entrada"])
        datos = resultado["resultado"]
        obtenido = Fraction(
            datos["numerador"],
            datos["denominador"]
        )

        assert obtenido == prueba["esperado"]
        assert datos["mixto"] == prueba["mixto"]

        print(f"[APROBADA] {prueba['nombre']}")
        print(f"Resultado: {datos['mixto']}\n")
        aprobadas += 1

    print(f"Total: {aprobadas}/{len(pruebas)} pruebas aprobadas.")
