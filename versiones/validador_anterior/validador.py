from fractions import Fraction
import ast
import operator

# Operaciones matemáticas permitidas
OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def evaluar_expresion(nodo):
    """
    Interpreta una expresión matemática
    utilizando fracciones exactas.
    """

    # Números enteros
    if isinstance(nodo, ast.Constant):
        if type(nodo.value) is int:
            return Fraction(nodo.value)

    # Operaciones binarias
    elif isinstance(nodo, ast.BinOp):

        tipo_operador = type(nodo.op)

        if tipo_operador not in OPERADORES:
            raise ValueError("Operador no permitido.")

        izquierda = evaluar_expresion(nodo.left)
        derecha = evaluar_expresion(nodo.right)

        if tipo_operador == ast.Div:
            if derecha == 0:
                raise ZeroDivisionError(
                    "No se puede dividir entre cero."
                )

        return OPERADORES[tipo_operador](
            izquierda, derecha
        )

    # Números negativos
    elif isinstance(nodo, ast.UnaryOp):
        if isinstance(nodo.op, ast.USub):
            return -evaluar_expresion(nodo.operand)

        elif isinstance(nodo.op, ast.UAdd):
            return evaluar_expresion(nodo.operand)

    raise ValueError("Expresión matemática no válida.")


def calcular(expresion):
    """
    Convierte una expresión escrita en texto
    a un resultado matemático exacto.
    """
    arbol = ast.parse(expresion, mode="eval")

    return evaluar_expresion(arbol.body)


def validar_procedimiento(pasos):
    """
    Comprueba si el valor matemático se conserva
    entre los pasos del procedimiento.
    """
    resultados = []

    for paso in pasos:
        try:
            resultado = calcular(paso)
            resultados.append(resultado)

        except (ValueError, SyntaxError,
                ZeroDivisionError) as error:
            return {
                "valido": False,
                "mensaje": f"Error en la expresión: {error}"
            }

    for i in range(1, len(resultados)):
        if resultados[i] != resultados[i - 1]:
            return {
                "valido": False,
                "paso_error": i + 1,
                "mensaje": (
                    "El valor matemático cambió "
                    "entre dos pasos consecutivos."
                )
            }

    return {
        "valido": True,
        "mensaje": "El procedimiento conserva su valor matemático."
    }

# ==========================================
# PRUEBAS DEL VALIDADOR
# ==========================================
pruebas = [
    {
        "id": "V01",
        "descripcion": "Suma correcta",
        "pasos": [
            "2/3 + 1/4",
            "8/12 + 3/12",
            "11/12"
        ]
    },
    {
        "id": "V02",
        "descripcion": "Suma incorrecta",
        "pasos": [
            "2/3 + 1/4",
            "8/12 + 2/12",
            "10/12"
        ]
    },
    {
        "id": "V03",
        "descripcion": "Suma con fracciones equivalentes",
        "pasos": [
            "5/9 + 1/3",
            "5/9 + 3/9",
            "8/9"
        ]
    },
    {
        "id": "V04",
        "descripcion": "Resta correcta",
        "pasos": [
            "2/3 - 1/4",
            "8/12 - 3/12",
            "5/12"
        ]
    },
    {
        "id": "V05",
        "descripcion": "Multiplicacion correcta",
        "pasos": [
            "2/3 * 3/4",
            "6/12",
            "1/2"
        ]
    },
    {
        "id": "V06",
        "descripcion": "Division correcta",
        "pasos": [
            "2/3 / 4/5",
            "10/12",
            "5/6"
        ]
    },
    {
        "id": "V07",
        "descripcion": "Multiplicacion incorrecta",
        "pasos": [
            "2/3 * 3/4",
            "5/12"
        ]
    },
    {
        "id": "V08",
        "descripcion": "Division entre cero",
        "pasos": [
            "1/2 / 0"
        ]
    },
    {
        "id": "V09",
        "descripcion": "Resta con resultado negativo",
        "pasos": [
            "1/4 - 3/4",
            "-2/4",
            "-1/2"
        ]
    },
    {
        "id": "V10",
        "descripcion": "Operacion con parentesis",
        "pasos": [
            "(1/2 + 1/4)",
            "2/4 + 1/4",
            "3/4"
        ]
    },
    {
        "id": "V11",
        "descripcion": "Expresion incompleta",
        "pasos": [
            "2/3 +",
            "11/12"
        ]
    },
    {
        "id": "V12",
        "descripcion": "Fracciones equivalentes con distinto denominador",
        "pasos": [
            "1/2",
            "2/4",
            "3/6"
        ]
    }
]

# ==========================================
# EJECUCION DE LAS PRUEBAS
# ==========================================
for prueba in pruebas:
    print("\n" + "-" * 50)
    print(prueba["id"], "-", prueba["descripcion"])

    resultado = validar_procedimiento(prueba["pasos"])

    print("Procedimiento:")
    for numero, paso in enumerate(prueba["pasos"], start=1):
        print(f"  Paso {numero}: {paso}")

    print("Resultado:", resultado)



