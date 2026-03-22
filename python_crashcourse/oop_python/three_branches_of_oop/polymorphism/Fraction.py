import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('numerator must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('denominator must be an integer')
        self.numerator = numerator
        self.denominator = denominator

        greatestCommonDivisor = math.gcd(self.numerator, self.denominator)
        if greatestCommonDivisor > 1:
            self.numerator = numerator // greatestCommonDivisor
            self.denominator = denominator // greatestCommonDivisor
        self.value = self.numerator // self.denominator

        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        output = ' Fraction ' + str(self.numerator) + '/' +  str(self.denominator) + '\n' +  ' Value: ' + str(self.value)+ '\n'
        return output