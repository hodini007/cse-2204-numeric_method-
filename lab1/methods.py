"""Function-based versions of the lab 1 calculations."""

import math


def euler_step(derivative, t0, y0, h, steps):
    """Return values from explicit Euler integration, including the initial value."""
    values = [(t0, y0)]
    t, y = t0, y0
    for _ in range(steps):
        y += derivative(t, y) * h
        t += h
        values.append((t, y))
    return values


def finite_difference(function, x, h):
    """Return forward, backward, and centered finite differences at ``x``."""
    forward = (function(x + h) - function(x)) / h
    backward = (function(x) - function(x - h)) / h
    centered = (function(x + h) - function(x - h)) / (2 * h)
    return forward, backward, centered


def machine_epsilon(kind=float):
    """Return machine epsilon for ``float`` or a NumPy floating type."""
    one = kind(1.0)
    epsilon = kind(1.0)
    while one + epsilon / kind(2.0) > one:
        epsilon /= kind(2.0)
    return epsilon


def exponential_series(x, significant_digits=4, max_terms=100):
    """Approximate ``exp(x)`` with a Taylor series until the stopping criterion."""
    stopping_error = 0.5 * 10 ** (2 - significant_digits)
    total, term, approximate_error = 0.0, 1.0, math.inf
    terms = 0
    while terms < max_terms:
        total += term
        terms += 1
        approximate_error = abs(term / total) * 100
        term = term * x / terms
        if terms > 1 and approximate_error < stopping_error:
            break
    return total, terms, approximate_error


def taylor_approximation(coefficients, h):
    """Evaluate a Taylor polynomial from derivative values at the expansion point."""
    estimate = 0.0
    power = 1.0
    for order, derivative in enumerate(coefficients):
        estimate += derivative / math.factorial(order) * power
        power *= h
    return estimate