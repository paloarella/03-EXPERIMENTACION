
from validador.codigo.modelo_fraccion import Fraccion

def probar_normalizacion():
    casos = [
        (2, 4, "1/2"),
        (6, 8, "3/4"),
        (-2, 4, "-1/2"),
        (2, -4, "-1/2"),
        (-2, -4, "1/2"),
        (0, 5, "0"),
        (10, 5, "2"),
    ]

    for n, d, esperado in casos:
        resultado = Fraccion(n, d)
        assert str(resultado) == esperado, (
            f"Error con {n}/{d}: se obtuvo {resultado}"
        )
    print(f"[APROBADA] {len(casos)} casos de normalización")


def probar_denominador_cero():
    try:
        Fraccion(2, 0)
    except ValueError:
        print("[APROBADA] Rechazo de denominador cero")
    else:
        raise AssertionError("Se aceptó un denominador igual a cero.")

def probar_tipos_invalidos():
    try:
        Fraccion(2.5, 4)
    except TypeError:
        print("[APROBADA] Rechazo de valores no enteros")
    else:
        raise AssertionError("Se aceptó un numerador decimal.")

if __name__ == "__main__":
    probar_normalizacion()
    probar_denominador_cero()
    probar_tipos_invalidos()