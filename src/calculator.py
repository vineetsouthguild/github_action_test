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

    def percentage(self, value, percent):
        """Calculate percentage of a value."""
        return (value * percent) / 100

