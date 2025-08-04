"""
Test cases for the Calculator class and utility functions
"""

import pytest
from src.calculator import Calculator, fibonacci, is_prime, factorial


class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(2.5, 1.5) == 4.0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, 1) == -2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(2.5, 1.5) == 1.0
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.multiply(2.5, 2) == 5.0
    
    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-8, -2) == 4
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(10, 1) == 10
        assert self.calc.power(-2, 3) == -8
        assert self.calc.power(2, -2) == 0.25
    
    def test_square_root(self):
        """Test square root operation."""
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(16) == 4
        assert self.calc.square_root(0) == 0
        assert self.calc.square_root(2) == pytest.approx(1.414, rel=1e-3)
    
    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)


class TestUtilityFunctions:
    """Test cases for utility functions."""
    
    def test_fibonacci(self):
        """Test Fibonacci number generation."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55
    
    def test_fibonacci_negative(self):
        """Test Fibonacci with negative input raises ValueError."""
        with pytest.raises(ValueError, match="Fibonacci number cannot be negative"):
            fibonacci(-1)
    
    def test_is_prime(self):
        """Test prime number checking."""
        # Test prime numbers
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(17) == True
        
        # Test non-prime numbers
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False
        
        # Test edge cases
        assert is_prime(0) == False
        assert is_prime(-1) == False
    
    def test_factorial(self):
        """Test factorial calculation."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
    
    def test_factorial_negative(self):
        """Test factorial with negative input raises ValueError."""
        with pytest.raises(ValueError, match="Factorial cannot be calculated for negative numbers"):
            factorial(-1)


class TestIntegration:
    """Integration tests combining multiple functions."""
    
    def test_calculator_with_factorial_result(self):
        """Test using factorial result in calculator operations."""
        calc = Calculator()
        fact_5 = factorial(5)  # 120
        assert calc.add(fact_5, 10) == 130
        assert calc.divide(fact_5, 5) == 24
    
    def test_fibonacci_prime_check(self):
        """Test checking if Fibonacci numbers are prime."""
        fib_numbers = [fibonacci(i) for i in range(1, 8)]  # [1, 1, 2, 3, 5, 8, 13]
        prime_fibs = [num for num in fib_numbers if is_prime(num)]
        assert prime_fibs == [2, 3, 5, 13]
