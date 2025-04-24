def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

class ImaginaryNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    
    def __add__(self, other):
        return ImaginaryNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return ImaginaryNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ImaginaryNumber(real, imag)
    
    def conjugate(self):
        return ImaginaryNumber(self.real, -self.imag)

a = ImaginaryNumber(1, 2)
b = ImaginaryNumber(3, 4)
print(a + b)
print(a - b)
print(a * b)
print(a.conjugate())
