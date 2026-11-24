"""Mindey symbolic-math profile for fxy."""

__fxy_profile__ = 1
__requires__ = [
    "sympy>=1.13",
    "mpmath>=1.3",
]

import sympy as sp

from sympy import (
    E,
    I,
    Eq,
    Matrix,
    Symbol,
    diff,
    expand,
    factor,
    integrate,
    limit,
    oo,
    pi,
    series,
    simplify,
    solve,
    solveset,
    sqrt,
    symbols,
)
from mpmath import mp
