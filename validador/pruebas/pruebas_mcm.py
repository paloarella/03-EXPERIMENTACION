from math import gcd
from validador.codigo.mcm import calcular_mcm, validar_mcm

def probar_mcm():
    casos = [
        (3, 4, 12),
        (6, 8, 24),
        (5, 10, 10),
        (7, 9, 63),
        (12, 18, 36),
        (1, 5, 5),
        (0, 5, 0),
        (-3, 4, 12),
        (-6, -8, 24),
    ]

    for a, b, esperado in casos:
        obtenido = calcular_mcm(a, b)

        assert obtenido == esperado, (
            f"Error: MCM({a}, {b}) = {obtenido}; "
            f"se esperaba {esperado}"
        )

        assert validar_mcm(a, b, esperado)
    print(f"[APROBADA] {len(casos)} casos de MCM")

if __name__ == "__main__":
    probar_mcm()