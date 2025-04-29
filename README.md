# Polynomial Handler: OOP Demo (Could be a calc or a lib in the future)

## 📜 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Code Breakdown](#-code-breakdown)
- [Usage Examples](#-usage-examples)
- [Potential Upgrades](#-potential-upgrades)
- [Credits](#-credits)
- [License](#-license)

## Overview

This script provides three core classes for mathematical operations:

1. **`Fraction`**: Implements rational numbers with GCD simplification
2. **`Integer`**: Subclass of `Fraction` for whole numbers
3. **`Monomial`**: Handles expressions of form _axⁿ_ with Fraction coefficients

Built with strict **encapsulation** and **operator overloading**, it enables:

m = Monomial(Fraction(5,2), 6)
n = Monomial(Integer(7), 6)
print(m + n) # Output: 19/2x⁶

## Features

### - Fraction Class

Euclidean algorithm for GCD

Full arithmetic operations (+, -, \*, /)

Automatic simplification

Encapsulated numerator/denominator

### - Integer Subclass

Inherits Fraction functionality

Denominator fixed at 1

Clean string representation

### - Monomial Class

Type-safe coefficient/degree handling

Degree-matching validation for operations

Zero monomial detection

Error handling for invalid operations

## Code Breakdown

### Fraction Class (source)

python
class Fraction:
def **gcf(self): # Euclidean algorithm implementation
a, b = abs(self.**num), abs(self.\_\_denom)
while b: a, b = b, a % b
return a
Key Methods:

simplify(): Reduces fraction using GCD

Arithmetic operators: Return new Fraction instances

Getters: Enforce encapsulation

### Monomial Operations (source)

python
def **add**(self, other):
if self.degree != other.degree:
print("error") # Future: Raise exception
return None
return Monomial(self.coeff + other.coeff, self.degree)

## Usage Examples

#### Basic Fraction Operations

python
f1 = Fraction(3, 4)
f2 = Fraction(2, 5)
print(f1 \* f2) # 6/20 → Simplified to 3/10

#### Monomial Mathematics

python
m = Monomial(Fraction(5,2), 6) # ⁵⁄₂x⁶
n = Monomial(Integer(7), 6) # 7x⁶

print(m + n) # ¹⁹⁄₂x⁶
print(m \* n) # ³⁵⁄₂x¹²
print(m / n) # ⁵⁄₁₄x⁰ → ⁵⁄₁₄

## Potential Upgrades (Any ideas/requests appreciated)

#### Polynomial Class

- Support for multi-term expressions
- Factorization algorithms
- Root finding methods
- Enhanced Arithmetic
- Mixed-type operations (Fraction \* Integer)
- Power operations for monomials
- Cross-type comparisons
- Serialization
- JSON I/O support
- LaTeX formatting
- Pretty-print options

# Credits

## Developed by TilinSolutions

### Core Team:

#### xuyaxaki: Absolutely did not do everything because it was an assignment

#### Akoza: Akoza

#### House: Si

#### Peppy: Literally the Abrahamic god

## WHY THIS CODE?

##### Encapsulation: Private variables stay hidden.

##### Flexibility: Mix Fraction and Integer.

## License

#### MIT License © 2024 TilinSolutions

Special thanks to Canaway Private School 2024-2025 for the problem statement, and actually the whole idea.
Disclaimer: The original assignment ain't mine. Also the code sucks.
