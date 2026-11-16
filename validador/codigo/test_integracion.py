
import sys
from pathlib import Path

# Permite importar los módulos de la carpeta codigo
RUTA_CODIGO = Path(__file__).resolve().parents[1] / "codigo"
sys.path.insert(0, str(RUTA_CODIGO))

from integrar_suma import integrar_suma
from integrar_resta import integrar_resta
from integrar_multiplicacion import integrar_multiplicacion
from integrar_division import integrar_division


def ejecutar_prueba(nombre, funcion, datos, esperado):
    resultado = funcion(datos)
    estado = resultado.get("estado")

    correcto = estado == esperado

    print(f"\n{nombre}")
    print(f"Esperado: {esperado}")
    print(f"Obtenido: {estado}")
    print("Resultado:", "APROBADA" if correcto else "FALLIDA")
    print("Mensaje:", resultado.get("mensaje"))

    return correcto


# Datos base de cada operación
suma = {
    "numerador1": 4,
    "denominador1": 15,
    "numerador2": 3,
    "denominador2": 20,
    "mcm_estudiante": 60,
    "numerador1_equivalente": 16,
    "denominador1_equivalente": 60,
    "numerador2_equivalente": 9,
    "denominador2_equivalente": 60,
    "resultado_numerador": 25,
    "resultado_denominador": 60,
    "numerador_simplificado": 5,
    "denominador_simplificado": 12
}

resta = {
    "entero1": 1,
    "numerador1": 2,
    "denominador1": 9,
    "entero2": 0,
    "numerador2": 4,
    "denominador2": 9,
    "mcm_estudiante": 9,
    "n1_equivalente": 2,
    "d1_equivalente": 9,
    "n2_equivalente": 4,
    "d2_equivalente": 9,
    "numerador_entero": 9,
    "denominador_entero": 9,
    "requiere_prestamo": True,
    "entero_prestamo": 0,
    "numerador_prestamo": 11,
    "denominador_prestamo": 9,
    "entero_resultado": 0,
    "numerador_resultado": 7,
    "denominador_resultado": 9
}

multiplicacion = {
    "numerador1": 1,
    "denominador1": 5,
    "numerador2": 5,
    "denominador2": 6,
    "n1_cruzado": 1,
    "d1_cruzado": 1,
    "n2_cruzado": 1,
    "d2_cruzado": 6,
    "numerador_resultado": 1,
    "denominador_resultado": 6
}

division = {
    "es_mixto": True,
    "entero1": 2,
    "numerador1": 2,
    "denominador1": 5,
    "numerador_impropio": 12,
    "denominador_impropio": 5,
    "numerador2": 8,
    "denominador2": 15,
    "numerador_inverso": 15,
    "denominador_inverso": 8,
    "n1_cruzado": 3,
    "d1_cruzado": 1,
    "n2_cruzado": 3,
    "d2_cruzado": 2,
    "entero_resultado": 4,
    "numerador_resultado": 1,
    "denominador_resultado": 2
}


if __name__ == "__main__":
#pruebas positivas
    pruebas = [
        ("Suma correcta", integrar_suma, suma, "correcto"),
        ("Resta correcta", integrar_resta, resta, "correcto"),
        ("Multiplicación correcta", integrar_multiplicacion,
         multiplicacion, "correcto"),
        ("División correcta", integrar_division, division, "correcto")
    ]

    aprobadas = 0

    print("========== PRUEBAS DE INTEGRACIÓN ==========")

    for nombre, funcion, datos, esperado in pruebas:
        if ejecutar_prueba(nombre, funcion, datos, esperado):
            aprobadas += 1

    print("\n========== RESUMEN ==========")
    print(f"Pruebas aprobadas: {aprobadas}/{len(pruebas)}")
    print(f"Pruebas fallidas: {len(pruebas) - aprobadas}")

#pruebas negativas

    print("\n========== PRUEBAS DE ERRORES ==========")

    pruebas_error = [
        (
            "Suma: MCM incorrecto",
            integrar_suma,
            {**suma, "mcm_estudiante": 120}
        ),
        (
            "Resta: préstamo incorrecto",
            integrar_resta,
            {**resta, "numerador_prestamo": 10}
        ),
        (
            "Multiplicación: simplificación cruzada incorrecta",
            integrar_multiplicacion,
            {**multiplicacion, "n1_cruzado": 2}
        ),
        (
            "División: inverso incorrecto",
            integrar_division,
            {**division, "numerador_inverso": 8}
        )
    ]

    for nombre, funcion, datos in pruebas_error:
        resultado = funcion(datos)

        print(f"\n{nombre}")
        print("Estado obtenido:", resultado.get("estado"))
        print("Paso identificado:", resultado.get("paso"))
        print("Mensaje:", resultado.get("mensaje"))

    print("\nResta: préstamo omitido")

    resta_sin_prestamo = {
        **resta,
        "requiere_prestamo": False
    }

    resultado = integrar_resta(resta_sin_prestamo)

    print("Estado obtenido:", resultado.get("estado"))
    print("Paso identificado:", resultado.get("paso"))
    print("Mensaje:", resultado.get("mensaje"))

