"""Interpolation and finite-difference methods."""

from .finite_differences import backward_diff_table, forward_diff_table
from .gauss_central import gauss_backward, gauss_forward
from .inverse_interpolation import inverse_lagrange
from .lagrange import lagrange
from .newton_banckward import newton_backward
from .newton_forward import newton_forward
from .sterling import stirling

__all__ = [name for name in globals() if not name.startswith("_")]