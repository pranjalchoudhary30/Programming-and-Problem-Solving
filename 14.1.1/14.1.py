class Complex:
    def initComplex(self):
        self.real, self.imag = map(int, input().split())

    def sum(self, c1, c2):
        self.real = c1.real + c2.real
        self.imag = c1.imag + c2.imag

    def display(self):
        if self.imag >= 0:
            print(self.real, "+", str(self.imag) + "i")
        else:
            print(self.real, "-", str(abs(self.imag)) + "i")


c1 = Complex()
c2 = Complex()
result = Complex()

c1.initComplex()
c2.initComplex()

result.sum(c1, c2)
result.display()
