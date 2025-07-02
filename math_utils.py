import math
from typing import List, Union, Optional, Sequence
from functools import reduce
import operator


class MathUtils:
    """A collection of mathematical utility functions."""
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of a non-negative integer."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n - 1)
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """Calculate the nth Fibonacci number (0-indexed)."""
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def fibonacci_sequence(n: int) -> List[int]:
        """Generate the first n Fibonacci numbers."""
        if n <= 0:
            return []
        if n == 1:
            return [0]
        
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Find all prime factors of a number."""
        if n <= 1:
            return []
        
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Calculate the Greatest Common Divisor using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Calculate the Least Common Multiple."""
        return abs(a * b) // MathUtils.gcd(a, b) if a and b else 0
    
    @staticmethod
    def power(base: Union[int, float], exponent: int) -> Union[int, float]:
        """Calculate base raised to the power of exponent."""
        if exponent == 0:
            return 1
        if exponent < 0:
            return 1 / MathUtils.power(base, -exponent)
        
        result = 1
        for _ in range(abs(exponent)):
            result *= base
        return result
    
    @staticmethod
    def square_root(n: Union[int, float], precision: float = 1e-10) -> float:
        """Calculate square root using Newton's method."""
        if n < 0:
            raise ValueError("Square root is not defined for negative numbers")
        if n == 0:
            return 0
        
        x = n
        while True:
            root = 0.5 * (x + n / x)
            if abs(root - x) < precision:
                break
            x = root
        return root
    
    @staticmethod
    def mean(numbers: Sequence[Union[int, float]]) -> float:
        """Calculate the arithmetic mean of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def median(numbers: Sequence[Union[int, float]]) -> float:
        """Calculate the median of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        
        if n % 2 == 0:
            return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            return sorted_numbers[n//2]
    
    @staticmethod
    def mode(numbers: Sequence[Union[int, float]]) -> List[Union[int, float]]:
        """Find the mode(s) of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")
        
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        
        max_freq = max(frequency.values())
        return [num for num, freq in frequency.items() if freq == max_freq]
    
    @staticmethod
    def standard_deviation(numbers: Sequence[Union[int, float]]) -> float:
        """Calculate the standard deviation of a list of numbers."""
        if len(numbers) < 2:
            raise ValueError("Standard deviation requires at least 2 numbers")
        
        mean_val = MathUtils.mean(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / (len(numbers) - 1)
        return math.sqrt(variance)
    
    @staticmethod
    def combination(n: int, r: int) -> int:
        """Calculate nCr (combinations)."""
        if r > n or r < 0:
            return 0
        if r == 0 or r == n:
            return 1
        
        r = min(r, n - r)  # Take advantage of symmetry
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    
    @staticmethod
    def permutation(n: int, r: int) -> int:
        """Calculate nPr (permutations)."""
        if r > n or r < 0:
            return 0
        if r == 0:
            return 1
        
        result = 1
        for i in range(n, n - r, -1):
            result *= i
        return result
    
    @staticmethod
    def is_perfect_square(n: int) -> bool:
        """Check if a number is a perfect square."""
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    @staticmethod
    def sum_of_digits(n: int) -> int:
        """Calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(abs(n)))
    
    @staticmethod
    def reverse_number(n: int) -> int:
        """Reverse the digits of a number."""
        sign = -1 if n < 0 else 1
        return sign * int(str(abs(n))[::-1])


def main():
    """Demonstrate the math utility functions with examples."""
    print("=== Math Utils Example ===\n")
    
    # Basic number operations
    print("1. Basic Number Operations:")
    print(f"   Factorial of 5: {MathUtils.factorial(5)}")
    print(f"   10th Fibonacci number: {MathUtils.fibonacci(10)}")
    print(f"   First 10 Fibonacci numbers: {MathUtils.fibonacci_sequence(10)}")
    print(f"   Is 17 prime? {MathUtils.is_prime(17)}")
    print(f"   Prime factors of 60: {MathUtils.prime_factors(60)}")
    print(f"   GCD of 48 and 18: {MathUtils.gcd(48, 18)}")
    print(f"   LCM of 12 and 8: {MathUtils.lcm(12, 8)}")
    print(f"   2^10: {MathUtils.power(2, 10)}")
    print(f"   Square root of 25: {MathUtils.square_root(25)}\n")
    
    # Statistical operations
    print("2. Statistical Operations:")
    numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
    print(f"   Numbers: {numbers}")
    print(f"   Mean: {MathUtils.mean(numbers):.2f}")
    print(f"   Median: {MathUtils.median(numbers)}")
    print(f"   Mode: {MathUtils.mode(numbers)}")
    print(f"   Standard deviation: {MathUtils.standard_deviation(numbers):.2f}\n")
    
    # Combinatorics
    print("3. Combinatorics:")
    print(f"   5C3 (combinations): {MathUtils.combination(5, 3)}")
    print(f"   5P3 (permutations): {MathUtils.permutation(5, 3)}\n")
    
    # Number properties
    print("4. Number Properties:")
    print(f"   Is 16 a perfect square? {MathUtils.is_perfect_square(16)}")
    print(f"   Sum of digits of 12345: {MathUtils.sum_of_digits(12345)}")
    print(f"   Reverse of 12345: {MathUtils.reverse_number(12345)}\n")
    
    # Edge cases and error handling
    print("5. Edge Cases:")
    try:
        print(f"   Factorial of -1: {MathUtils.factorial(-1)}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    try:
        print(f"   Square root of -4: {MathUtils.square_root(-4)}")
    except ValueError as e:
        print(f"   Error: {e}")


if __name__ == "__main__":
    main()