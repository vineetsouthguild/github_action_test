"""
Performance tests for the Calculator class
These tests measure the performance of our mathematical functions
"""

import pytest
from src.calculator import Calculator, fibonacci, factorial, is_prime


class TestPerformance:
    """Performance benchmarks for calculator functions."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_fibonacci_performance(self, benchmark):
        """Benchmark Fibonacci number calculation."""
        result = benchmark(fibonacci, 20)
        assert result == 6765
    
    def test_factorial_performance(self, benchmark):
        """Benchmark factorial calculation."""
        result = benchmark(factorial, 10)
        assert result == 3628800
    
    def test_prime_check_performance(self, benchmark):
        """Benchmark prime number checking."""
        result = benchmark(is_prime, 97)
        assert result == True
    
    def test_gcd_performance(self, benchmark):
        """Benchmark GCD calculation."""
        result = benchmark(self.calc.gcd, 1071, 462)
        assert result == 21
    
    def test_trigonometric_performance(self, benchmark):
        """Benchmark trigonometric calculations."""
        result = benchmark(self.calc.sin, 45)
        assert abs(result - 0.7071) < 0.01
    
    @pytest.mark.parametrize("number", [100, 1000, 10000])
    def test_sum_of_digits_performance(self, benchmark, number):
        """Benchmark sum of digits for different number sizes."""
        from src.calculator import sum_of_digits
        result = benchmark(sum_of_digits, number)
        assert result > 0
