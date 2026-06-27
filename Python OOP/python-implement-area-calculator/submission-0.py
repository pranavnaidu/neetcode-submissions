import math

class AreaCalc:
    # TODO: Implement calculate method
    pass

    def calculate(self, length: int, width = None):
        if width is not None: 
            return length * width
        else: 
            n = ((length ** 2) * math.pi)
            return round(n, 2)
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
