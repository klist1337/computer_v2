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
        if self.real > 0 and self.imag > 0:
            return f"{self.real} + {self.imag}i"
        if self.real == 0 and self.imag == 0:
            return f"{self.real}"
        elif self.real == 0:
            return f"{self.imag}"
        elif self.imag == 0:
            return f"{self.real}i"
        return f"0"