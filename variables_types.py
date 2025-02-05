class RationnalNumber :
    def __init__(self, value):
        self .value = value

    def __str__(self):
        return f"{self.value}"



class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def format(self):
        if int(self.real) > 0:
            return f"{self.real} + {self.imag}i"
        elif int(self.real) == 0:
            return f"{self.imag}"
        elif int(self.imag) == 0:
            return f"{self.real}i"
        return f"{self.real} - {self.imag}i"