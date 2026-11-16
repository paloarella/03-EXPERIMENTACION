from dataclasses import dataclass
from math import gcd

@dataclass(frozen=True)
class Fraccion:
    numerador: int
    denominador: int

    def __post_init__(self):
        if type(self.numerador) is not int or type(self.denominador) is not int:
            raise TypeError("El numerador y el denominador deben ser enteros.")

        if self.denominador == 0:
            raise ValueError("El denominador no puede ser cero.")

        # Mantener siempre el denominador positivo.
        n = self.numerador
        d = self.denominador

        if d < 0:
            n = -n
            d = -d

        # Simplificar la fracción.
        divisor = gcd(abs(n), d)
        n //= divisor
        d //= divisor

        # Guardar los valores normalizados.
        object.__setattr__(self, "numerador", n)
        object.__setattr__(self, "denominador", d)

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"

    def es_entero(self):
        return self.denominador == 1
