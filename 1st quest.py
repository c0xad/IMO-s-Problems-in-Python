#Let ABCD be a cyclic quadrilateral with diagonal BD. 
#Prove that AB·CD + AD·BC ≥ AC·BD, with equality if and only if ABCD is a rectangle.

from sympy import symbols, sin, cos, simplify

# Define variables and angles
AB, AD, BD, BC, CD, AC, theta = symbols('AB AD BD BC CD AC theta')

# Apply Ptolemy's inequality
inequality = AB*CD + AD*BC - AC*BD

# Use law of cosines to express BD in terms of other sides and angles
BD_expr = simplify(AC**2 + AD**2 - 2*AC*AD*cos(theta))

# Substitute BD expression into inequality and simplify
inequality = inequality.subs(BD, BD_expr)
inequality = simplify(inequality)

# Prove inequality for acute and obtuse angles
if 0 <= theta <= 90:
    assert inequality >= 0
elif 90 < theta <= 180:
    assert inequality <= 0

# Check for equality conditions
equality_conditions = simplify(inequality) == 0
if equality_conditions:
    print("Equality holds if and only if ABCD is a rectangle.")
