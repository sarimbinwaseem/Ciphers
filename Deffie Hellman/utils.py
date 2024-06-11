class DH_UTILS:
    def __init__(self, prime_number):
        self.prime_number = prime_number

    def _primitive_root(self):
        START_VALUE = 2
        POWER = 0
        END_VALUE = self.prime_number  # For loop, because for loop excludes last number.

        # roots = {}
        # roots = [[pow(base, power) % self.prime_number for power in range(0, END_VALUE)] for base in range(START_VALUE, END_VALUE)]
        # print(roots)
        for base in range(START_VALUE, END_VALUE):
            for power in range(0, END_VALUE):
                result = pow(base, power) % self.prime_number
                print(f"{base}^{power} % {self.prime_number} = {result}")
            print()
