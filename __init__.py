"""Reusable numerical methods from the coursework labs."""

from .lab1 import (
    euler_step,
    exponential_series,
    finite_difference,
    machine_epsilon,
    taylor_approximation,
)
from .lab2 import (
    aitken,
    bisection,
    false_position,
    fixed_point,
    generalized_newton,
    iteration_system,
    newton_raphson,
    newton_system,
    ramanujan,
    secant,
)
from .lab3 import (
    backward_diff_table,
    forward_diff_table,
    gauss_backward,
    gauss_forward,
    inverse_lagrange,
    lagrange,
    newton_backward,
    newton_forward,
    stirling,
)
from .lab4 import (
    multiple_linear_fit,
    non_linear_fit,
    polynomial_fit,
    straight_line_fit,
)

__all__ = [name for name in globals() if not name.startswith("_")]