import math

class AlgoritmEc:
    def __init__(self: 'AlgoritmEc') -> None:
        self.aBC = None
        self.x0 = None
        self.x1 = None
        self.x2 = None

    def cuadratica(self: 'AlgoritmEc', aBC: list[float]) -> tuple[float]:
        self.aBC = aBC
        if self.aBC[1]**2 >= 4*self.aBC[0]*self.aBC[2]:
            self.x1 = (-(self.aBC[1]) + math.sqrt(self.aBC[1]**2 - 4*self.aBC[0]*self.aBC[2])) / (2*self.aBC[0])
            self.x2 = (-(self.aBC[1]) - math.sqrt(self.aBC[1]**2 - 4*self.aBC[0]*self.aBC[2])) / (2*self.aBC[0])
            return self.x1, self.x2
        raise ValueError("[x] Error!, no real roots, discriminant < to 0.")

    def f(self, x:float) -> float:
        return self.aBC[0] * x**2 + self.aBC[1] * x - self.aBC[2]

    def valuesAB(self:'AlgoritmEc') -> None:
        print()
        while True:
            try:
                self.x0 = float(input("[+] Valor de x_0:> "))
                self.x1 = float(input("[+] Valor de x_1:> "))
                break
            except Exception as e:
                continue

    def tecnic_Secante(self:'AlgoritmEc', aBC: list[float], max_iter: int = 100, tol=1e-6, ) -> list[dict[str, float]]:
        self.aBC = aBC
        self.valuesAB() #self.x0, self.x1 = 1, 7

        iterations = list()
        for i in range(1, max_iter+1):
            fx0 , fx1 = self.f(self.x0), self.f(self.x1)

            if fx1 - fx0 == 0:
                raise ValueError("[x] Error, divicion by zero in secant formula")

            self.x2 = self.x1 - fx1 * (self.x1 - self.x0) / (fx1 - fx0)
            fx2 = self.f(self.x2)

            error_relativo = abs((self.x2 - self.x1) / self.x2) if self.x2 != 0 else None

            iterations.append({
                "iteration": i,
                "x_i-2": self.x0,
                "f(x_i-2)": fx0,
                "x_i-1": self.x1,
                "f(x_i-1)": fx1,
                "x_i": self.x2,
                "f(x_i)": fx2,
                "e_r_norm": error_relativo
            })

            if error_relativo is not None and error_relativo < tol:
                raise ValueError("[x] Error relativo alcanzado.")

            self.x0, self.x1 = self.x1, self.x2
        return iterations
