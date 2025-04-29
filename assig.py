# Fraction Class

class Fraction:
    __num = None   
    __denom = None  

    def __init__(self, num, denom):
        self.__num = num
        self.__denom = denom

    def __mul__(self, other):
        return Fraction(self.__num * other.__num, self.__denom * other.__denom)

    def __str__(self):
        return f"{self.__num}/{self.__denom}"

    def __gcf(self):
        # Greatest Common Factor (GCD).
        a = abs(self.__num)
        b = abs(self.__denom)
        while b != 0:
            a, b = b, a % b  # Euclidean algorithm
        return a

    def simplify(self):
        gcf = self.__gcf()
        self.__num = self.__num // gcf
        self.__denom = self.__denom // gcf

    def get_num(self):
        return self.__num

    def get_denom(self):
        return self.__denom

    # Arithmetic Operations 
    def __add__(self, other):
        """Add two fractions: (a/b) + (c/d) = (ad + bc)/bd"""
        new_num = self.get_num() * other.get_denom() + other.get_num() * self.get_denom()
        new_denom = self.get_denom() * other.get_denom()
        return Fraction(new_num, new_denom)

    def __sub__(self, other):
        """Subtract two fractions: (a/b) - (c/d) = (ad - bc)/bd"""
        new_num = self.get_num() * other.get_denom() - other.get_num() * self.get_denom()
        new_denom = self.get_denom() * other.get_denom()
        return Fraction(new_num, new_denom)

    def __truediv__(self, other):
        """Divide two fractions: (a/b) / (c/d) = (a*d)/(b*c)"""
        new_num = self.get_num() * other.get_denom()
        new_denom = self.get_denom() * other.get_num()
        return Fraction(new_num, new_denom)

    __div__ = __truediv__  # Alias for Python 2 compatibility. (Made the mistake of not including compatibility checks only once. Got destroyed on Discord)
    
# Integer Class (Subclass)

class Integer(Fraction):
    def __init__(self, num):
        super().__init__(num, 1)  

    def __str__(self):
        # Override string representation to show only the numerator (no denominator).
        return f"{self.get_num()}"  
    
    
    
    
    
# Monomial Class

class Monomial:
    def __init__(self, coefficient, degree):
        self.__coefficient = coefficient
        self.__degree = degree

    def __str__(self):
        # String representation of the monomial. 
        coeff = self.__coefficient
        if coeff.get_num() == 0:  
            return "0"
        coeff_str = str(coeff)
        degree = self.__degree
        if degree == 0:
            return coeff_str  
        elif degree == 1:
            return f"{coeff_str}x" 
        else:
            return f"{coeff_str}x^{degree}"  

    def get_coeff(self):
        return self.__coefficient

    def get_degree(self):
        return self.__degree

    # Arithmetic Operations 
    def __add__(self, other):
        if self.get_degree() != other.get_degree():
            print("error")
            return None
        new_coeff = self.get_coeff() + other.get_coeff()  # Use Fraction's __add__
        return Monomial(new_coeff, self.get_degree())

    def __sub__(self, other):
        if self.get_degree() != other.get_degree():
            print("error")
            return None
        new_coeff = self.get_coeff() - other.get_coeff()  # Use Fraction's __sub__
        return Monomial(new_coeff, self.get_degree())

    def __mul__(self, other):
        # Multiply coefficients and add degrees.
        new_coeff = self.get_coeff() * other.get_coeff()  # Use Fraction's __mul__
        new_degree = self.get_degree() + other.get_degree()
        return Monomial(new_coeff, new_degree)

    def __truediv__(self, other):
        if other.get_coeff().get_num() == 0:  # Check for division by zero
            print("error")
            return None
        new_coeff = self.get_coeff() / other.get_coeff()  # Use Fraction's __div__
        new_degree = self.get_degree() - other.get_degree()
        return Monomial(new_coeff, new_degree)

    __div__ = __truediv__  