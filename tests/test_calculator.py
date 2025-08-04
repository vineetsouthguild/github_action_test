"""
Test cases for the Calculator class and utility functions
"""

import pytest
from src.calculator import Calculator, fibonacci, is_prime, factorial, lucas_number, is_perfect_square, sum_of_digits, reverse_number, is_palindrome_number


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
    
    def test_percentage(self):
        """Test percentage calculation."""
        assert self.calc.percentage(100, 50) == 50
        assert self.calc.percentage(200, 25) == 50
        assert self.calc.percentage(80, 10) == 8
        assert self.calc.percentage(150, 33.33) == pytest.approx(49.995, rel=1e-3)
    
    def test_logarithm(self):
        """Test logarithm calculation."""
        assert self.calc.logarithm(100) == pytest.approx(2.0, rel=1e-6)  # log10(100) = 2
        assert self.calc.logarithm(8, 2) == pytest.approx(3.0, rel=1e-6)  # log2(8) = 3
        assert self.calc.logarithm(1) == pytest.approx(0.0, rel=1e-6)  # log(1) = 0
        
    def test_logarithm_errors(self):
        """Test logarithm error cases."""
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.logarithm(0)
        with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
            self.calc.logarithm(-5)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            self.calc.logarithm(10, 1)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            self.calc.logarithm(10, -2)
    
    def test_gcd(self):
        """Test Greatest Common Divisor calculation."""
        assert self.calc.gcd(48, 18) == 6
        assert self.calc.gcd(7, 5) == 1
        assert self.calc.gcd(-12, 8) == 4
        assert self.calc.gcd(0, 5) == 5
        assert self.calc.gcd(100, 25) == 25
    
    def test_lcm(self):
        """Test Least Common Multiple calculation."""
        assert self.calc.lcm(4, 6) == 12
        assert self.calc.lcm(7, 5) == 35
        assert self.calc.lcm(0, 5) == 0
        assert self.calc.lcm(12, 18) == 36
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test common angles
        assert self.calc.sin(0) == pytest.approx(0.0, abs=1e-6)
        assert self.calc.sin(90) == pytest.approx(1.0, abs=1e-6)
        assert self.calc.cos(0) == pytest.approx(1.0, abs=1e-6)
        assert self.calc.cos(90) == pytest.approx(0.0, abs=1e-6)
        assert self.calc.tan(0) == pytest.approx(0.0, abs=1e-6)
        assert self.calc.tan(45) == pytest.approx(1.0, abs=1e-6)


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
    
    def test_lucas_number(self):
        """Test Lucas number generation."""
        assert lucas_number(0) == 2
        assert lucas_number(1) == 1
        assert lucas_number(2) == 3
        assert lucas_number(3) == 4
        assert lucas_number(4) == 7
        assert lucas_number(5) == 11
        assert lucas_number(10) == 123
    
    def test_lucas_number_negative(self):
        """Test Lucas number with negative input raises ValueError."""
        with pytest.raises(ValueError, match="Lucas number cannot be negative"):
            lucas_number(-1)
    
    def test_is_perfect_square(self):
        """Test perfect square checking."""
        assert is_perfect_square(0) == True
        assert is_perfect_square(1) == True
        assert is_perfect_square(4) == True
        assert is_perfect_square(9) == True
        assert is_perfect_square(16) == True
        assert is_perfect_square(25) == True
        assert is_perfect_square(2) == False
        assert is_perfect_square(3) == False
        assert is_perfect_square(8) == False
        assert is_perfect_square(-4) == False
    
    def test_sum_of_digits(self):
        """Test sum of digits calculation."""
        assert sum_of_digits(123) == 6
        assert sum_of_digits(456) == 15
        assert sum_of_digits(0) == 0
        assert sum_of_digits(-789) == 24
        assert sum_of_digits(1000) == 1
    
    def test_reverse_number(self):
        """Test number reversal."""
        assert reverse_number(123) == 321
        assert reverse_number(-456) == -654
        assert reverse_number(1000) == 1
        assert reverse_number(0) == 0
        assert reverse_number(7) == 7
    
    def test_is_palindrome_number(self):
        """Test palindrome number checking."""
        assert is_palindrome_number(121) == True
        assert is_palindrome_number(1221) == True
        assert is_palindrome_number(12321) == True
        assert is_palindrome_number(0) == True
        assert is_palindrome_number(7) == True
        assert is_palindrome_number(-121) == True
        assert is_palindrome_number(123) == False
        assert is_palindrome_number(1234) == False


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
    
    def test_mathematical_relationships(self):
        """Test relationships between different mathematical functions."""
        calc = Calculator()
        
        # Test GCD and LCM relationship: gcd(a,b) * lcm(a,b) = a * b
        a, b = 12, 18
        assert calc.gcd(a, b) * calc.lcm(a, b) == a * b
        
        # Test perfect squares with square root
        perfect_squares = [1, 4, 9, 16, 25, 36]
        for square in perfect_squares:
            assert is_perfect_square(square) == True
            assert calc.square_root(square) == int(calc.square_root(square))
        
        # Test palindromes with reverse
        palindromes = [121, 1221, 12321]
        for num in palindromes:
            assert is_palindrome_number(num) == True
            assert num == reverse_number(num)
    
    def test_lucas_fibonacci_relationship(self):
        """Test relationship between Lucas and Fibonacci numbers."""
        # Lucas numbers and Fibonacci numbers are related
        # L(n) = F(n-1) + F(n+1) for n >= 1
        for n in range(1, 8):
            lucas_n = lucas_number(n)
            fib_prev = fibonacci(n - 1) if n > 0 else 0
            fib_next = fibonacci(n + 1)
            assert lucas_n == fib_prev + fib_next

