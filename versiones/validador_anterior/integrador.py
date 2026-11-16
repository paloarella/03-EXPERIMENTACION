
from suma import (
    validar_conversion as validar_conversion_suma,
    validar_suma,
    validar_simplificacion as validar_simplificacion_suma
)

from resta import (
    validar_mcm_resta,
    validar_conversion_fracciones,
    validar_conversion_entero,
    validar_prestamo,
    validar_resta
)

from multiplicacion import (
    validar_simplificacion_cruzada as validar_cruzada_multiplicacion,
    validar_producto
)

from division import (
    validar_mixta_a_impropia,
    validar_inverso,
    validar_simplificacion_cruzada as validar_cruzada_division,
    validar_division
)

from retroalimentacion import generar_retroalimentacion


def integrar_resultado(resultado):
    """
    Convierte el resultado de cualquier validador
    en un mensaje para el estudiante.
    """
    return generar_retroalimentacion(resultado)


def validar_operacion(operacion, datos):
    """
    Selecciona el módulo correspondiente a la operación.

    operacion: suma, resta, multiplicacion o division.
    datos: diccionario con los datos necesarios.
    """

    validadores = {
        "suma": validar_suma,
        "resta": validar_resta,
        "multiplicacion": validar_producto,
        "division": validar_division
    }

    if operacion not in validadores:
        return {
            "valido": False,
            "mensaje": "La operación indicada no es compatible."
        }

    try:
        resultado = validadores[operacion](**datos)
        return integrar_resultado(resultado)

    except TypeError as error:
        return {
            "estado": "error",
            "mensaje": f"Faltan datos o hay parámetros incorrectos: {error}"
        }


# Pruebas de integración
if __name__ == "__main__":

    print("\n========== PRUEBA DE SUMA ==========")

    datos_suma = {
        "numerador1": 4,
        "numerador2": 3,
        "denominador_comun": 60,
        "resultado_numerador": 25,
        "resultado_denominador": 60
    }

    print(validar_operacion("suma", datos_suma))

    print("\n========== PRUEBA DE RESTA ==========")

    datos_resta = {
        "entero1": 1,
        "numerador1": 2,
        "denominador1": 9,
        "entero2": 0,
        "numerador2": 4,
        "denominador2": 9,
        "entero_resultado": 0,
        "numerador_resultado": 7,
        "denominador_resultado": 9
    }

    print(validar_operacion("resta", datos_resta))

    print("\n========== PRUEBA DE MULTIPLICACION ==========")

    datos_multiplicacion = {
        "numerador1": 1,
        "denominador1": 5,
        "numerador2": 5,
        "denominador2": 6,
        "numerador_resultado": 1,
        "denominador_resultado": 6
    }

    print(validar_operacion("multiplicacion", datos_multiplicacion))

    print("\n========== PRUEBA DE DIVISION ==========")

    datos_division = {
        "numerador1": 9,
        "denominador1": 10,
        "numerador2": 1,
        "denominador2": 8,
        "entero_resultado": 7,
        "numerador_resultado": 1,
        "denominador_resultado": 5
    }

    print(validar_operacion("division", datos_division))
