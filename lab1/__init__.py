"""Reusable first-lab numerical approximations."""

from .methods import (
    euler_step,
    exponential_series,
    finite_difference,
    machine_epsilon,
    taylor_approximation,
)

__all__ = [name for name in globals() if not name.startswith("_")]