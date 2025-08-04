#!/usr/bin/env python3
"""
Main application - Demo app for GitHub Actions learning
"""

from src.calculator import Calculator, fibonacci, is_prime, factorial


def main():
    """Main function to demonstrate the calculator functionality."""
    print("🧮 Welcome to the GitHub Actions Calculator Demo!")
    print("=" * 50)
    
    calc = Calculator()
    
    # Demonstrate basic operations
    print("\n📊 Basic Operations:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print(f"√25 = {calc.square_root(25)}")
    
    # Demonstrate advanced functions
    print("\n🔢 Advanced Functions:")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"10th Fibonacci number: {fibonacci(10)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 18 prime? {is_prime(18)}")
    
    print("\n✅ All operations completed successfully!")
    print("This demonstrates that our GitHub Actions workflow works! 🎉")


if __name__ == "__main__":
    main()
