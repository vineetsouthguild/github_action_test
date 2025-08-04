 #!/usr/bin/env python3
"""
Main application - Demo app for GitHub Actions learning
"""

from src.calculator import (
    Calculator, fibonacci, is_prime, factorial, lucas_number, 
    is_perfect_square, sum_of_digits, reverse_number, is_palindrome_number
)


def main():
    """Main function to demonstrate the calculator functionality."""
    print("🧮 Welcome to the Advanced GitHub Actions Calculator Demo!")
    print("=" * 60)
    
    calc = Calculator()
    
    # Demonstrate basic operations
    print("\n📊 Basic Operations:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"√25 = {calc.square_root(25)}")
    print(f"50% of 200 = {calc.percentage(200, 50)}")
    print(f"25% of 80 = {calc.percentage(80, 25)}")
    
    # Demonstrate advanced mathematical operations
    print("\n🔢 Advanced Mathematical Operations:")
    print(f"log₁₀(100) = {calc.logarithm(100):.2f}")
    print(f"log₂(8) = {calc.logarithm(8, 2):.2f}")
    print(f"GCD(48, 18) = {calc.gcd(48, 18)}")
    print(f"LCM(12, 18) = {calc.lcm(12, 18)}")
    
    # Demonstrate trigonometric functions
    print("\n📐 Trigonometric Functions:")
    print(f"sin(30°) = {calc.sin(30):.3f}")
    print(f"cos(60°) = {calc.cos(60):.3f}")
    print(f"tan(45°) = {calc.tan(45):.3f}")
    
    # Demonstrate utility functions
    print("\n🔢 Number Theory Functions:")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"10th Fibonacci number: {fibonacci(10)}")
    print(f"10th Lucas number: {lucas_number(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 16 a perfect square? {is_perfect_square(16)}")
    
    # Demonstrate number manipulation
    print("\n🔄 Number Manipulation:")
    print(f"Sum of digits in 12345: {sum_of_digits(12345)}")
    print(f"Reverse of 12345: {reverse_number(12345)}")
    print(f"Is 12321 a palindrome? {is_palindrome_number(12321)}")
    print(f"Is 12345 a palindrome? {is_palindrome_number(12345)}")
    
    # Demonstrate mathematical relationships
    print("\n🔗 Mathematical Relationships:")
    a, b = 12, 18
    gcd_val = calc.gcd(a, b)
    lcm_val = calc.lcm(a, b)
    print(f"For numbers {a} and {b}:")
    print(f"  GCD = {gcd_val}, LCM = {lcm_val}")
    print(f"  GCD × LCM = {gcd_val * lcm_val} = {a} × {b} = {a * b} ✓")
    
    # Show some interesting number sequences
    print("\n📈 Number Sequences:")
    print("First 10 Fibonacci numbers:", [fibonacci(i) for i in range(10)])
    print("First 10 Lucas numbers:", [lucas_number(i) for i in range(10)])
    print("Prime numbers up to 30:", [i for i in range(2, 31) if is_prime(i)])
    print("Perfect squares up to 100:", [i for i in range(1, 101) if is_perfect_square(i)])
    
    print("\n✅ All operations completed successfully!")
    print("🎉 This demonstrates our advanced GitHub Actions workflow!")
    print("🚀 Multiple jobs, matrix testing, security scans, and more!")


if __name__ == "__main__":
    main()
