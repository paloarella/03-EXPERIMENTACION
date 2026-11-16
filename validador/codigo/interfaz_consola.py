from validador.codigo.motor_matematico import operar_fracciones
from validador.codigo.generador_pasos import generar_explicacion

def solicitar_entero(mensaje):
    """Solicita un número entero y valida la entrada."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Escribe un número entero.")

def solicitar_fraccion(numero):
    """Solicita el numerador y denominador de una fracción."""
    print(f"\nIngresa la fracción {numero}:")
    numerador = solicitar_entero("Numerador: ")

    while True:
        denominador = solicitar_entero("Denominador: ")
        if denominador == 0:
            print("El denominador no puede ser cero.")
        else:
            break

    return numerador, denominador

def solicitar_operacion():
    """Permite seleccionar una operación matemática."""
    operaciones = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/"
    }

    print("\nSelecciona la operación:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    while True:
        opcion = input("Opción: ").strip()

        if opcion in operaciones:
            return operaciones[opcion]

        print("Opción no válida. Selecciona del 1 al 4.")


def mostrar_resultado(resultado):
    """Muestra los pasos y el resultado de la operación."""

    print("\n========== PROCEDIMIENTO ==========")

    for paso in resultado["explicacion"]:
        print(paso["texto"])

    print("\n========== RESULTADO FINAL ==========")
    print("Fracción:", resultado["resultado"]["fraccion"])
    print("Resultado:", resultado["resultado"]["mixto"])


def ejecutar_aplicacion():

    print("====================================")
    print("   APOYO AL APRENDIZAJE DE FRACCIONES")
    print("====================================")

    while True:
        try:
            n1, d1 = solicitar_fraccion(1)
            n2, d2 = solicitar_fraccion(2)
            operacion = solicitar_operacion()
            resultado_motor = operar_fracciones(
                n1, d1, n2, d2, operacion
            )
            explicacion = generar_explicacion(resultado_motor)
            mostrar_resultado(explicacion)

        except ZeroDivisionError as error:
            print("\nNo se pudo realizar la operación:", error)

        except (ValueError, TypeError) as error:
            print("\nNo se pudo procesar la entrada:", error)

        continuar = input(
            "\n¿Deseas resolver otra operación? (s/n): "
        ).strip().lower()

        if continuar != "s":
            print("\nGracias por utilizar la aplicación.")
            break

def main():
    ejecutar_aplicacion()

if __name__ == "__main__":
    ejecutar_aplicacion()