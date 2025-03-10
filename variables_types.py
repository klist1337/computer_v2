class RationnalNumber :
    def __init__(self, value):
        self .value = value

    def __str__(self):
        return f"{self.value}"



class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.real < 0:
             if self.imag < 0:
                return f"-{abs(self.real)} - {abs(self.imag)}i"
             elif self.imag > 0:
                return f"-{abs(self.real)} + {abs(self.imag)}i"
        elif self.real > 0:
            if self.imag > 0:
                return f"{abs(self.real)} + {abs(self.imag)}i"
            elif self.real > 0 and self.imag < 0:
                 return f"{abs(self.real)} - {abs(self.imag)}i"
        elif self.real == 0 :
            if self.imag == 0:
                return f"{abs(self.real)}"
            elif self.imag < 0:
                return f"-{abs(self.imag)}i"
            elif  self.imag > 0:
                return f"{abs(self.imag)}i"
        if self.imag == 0:
            if self.real < 0:
                return f"-{abs(self.real)}"
            elif self.real > 0:
                return f"{abs(self.real)}"
        return f"0"