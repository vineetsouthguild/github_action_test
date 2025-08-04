"""
Calculator module - A simple calculator for learning GitHub Actions
"""

class Calculator:
    """A simple calculator class with basic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5
    
    def percentage(self, value, percent):
        """Calculate percentage of a value."""
        return (value * percent) / 100
    
    def logarithm(self, number, base=10):
        """Calculate logarithm of a number with given base (default base 10)."""
        import math
        if number <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return math.log(number) / math.log(base)
    
    def gcd(self, a, b):
        """Calculate Greatest Common Divisor using Euclidean algorithm."""
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        """Calculate Least Common Multiple."""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)
    
    def sin(self, angle_degrees):
        """Calculate sine of angle in degrees."""
        import math
        return math.sin(math.radians(angle_degrees))
    
    def cos(self, angle_degrees):
        """Calculate cosine of angle in degrees."""
        import math
        return math.cos(math.radians(angle_degrees))
    
    def tan(self, angle_degrees):
        """Calculate tangent of angle in degrees."""
        import math
        return math.tan(math.radians(angle_degrees))


def fibonacci(n):
    """Generate nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial cannot be calculated for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def lucas_number(n):
    """Generate nth Lucas number (similar to Fibonacci but starts with 2, 1)."""
    if n < 0:
        raise ValueError("Lucas number cannot be negative")
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_number(n - 1) + lucas_number(n - 2)


def is_perfect_square(number):
    """Check if a number is a perfect square."""
    if number < 0:
        return False
    sqrt_num = int(number ** 0.5)
    return sqrt_num * sqrt_num == number


def sum_of_digits(number):
    """Calculate the sum of digits in a number."""
    return sum(int(digit) for digit in str(abs(number)))


def reverse_number(number):
    """Reverse the digits of a number."""
    sign = -1 if number < 0 else 1
    return sign * int(str(abs(number))[::-1])


def is_palindrome_number(number):
    """Check if a number is a palindrome."""
    return str(abs(number)) == str(abs(number))[::-1]

