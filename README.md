# Numeric Methods Collection

This folder contains Python implementations of classic numerical methods used in the coursework labs. The methods can be imported as a package, while the original scripts remain available as worked examples.

## Contents

- `lab2/bisection.py` - bisection method for scalar nonlinear equations
- `lab2/false_position.py` - false position method
- `lab2/fixed_pos.py` - fixed-point iteration
- `lab2/secant.py` - secant method
- `lab2/newton.py` - Newton-Raphson method for single equations
- `lab2/newton_for_system.py` - Newton-Raphson method for systems of nonlinear equations
- `lab2/iteration.py` - simple iteration method for systems
- `lab2/aitken.py` - Aitken acceleration
- `lab2/gen_newton.py` - generalized Newton-style examples
- `lab2/ramanujan.py` - Ramanujan-related numerical experiment

## Importing the package

From the repository root, install it once in editable mode:

```bash
python3 -m pip install -e .
```

Then import methods in any Python file:

```python
from numeric import bisection, newton_raphson, lagrange, straight_line_fit

root = bisection(lambda x: x**2 - 2, 0, 2, verbose=False)
value = lagrange([0, 1], [0, 1], 0.25)
line = straight_line_fit([(1, 2), (2, 4), (3, 6)])
```

Lab-specific imports are also available:

```python
from numeric.lab2 import secant
from numeric.lab3 import newton_forward
from numeric.lab4 import polynomial_fit
```

## Requirements

- Python 3.8 or later
- NumPy (used by the curve-fitting methods in `lab4`)

## How to Run

From the repository root, run any script directly with Python:

```bash
python3 numeric/lab2/newton.py
python3 numeric/lab2/bisection.py
python3 numeric/lab2/secant.py
python3 numeric/lab2/newton_for_system.py
```

Most scripts print the iteration steps and the final approximate root for several sample problems.

## Notes

- The scripts are organized by method, not by input/output library structure.
- Several files are classroom exercises, so the same method may appear in multiple variations.
- Import reusable functions from `numeric` or one of its lab packages instead of copying code.

## Suggested Workflow

1. Open the script for the method you want to study.
2. Review the function definition at the top of the file.
3. Run the file to inspect the iteration trace.
4. Modify the initial guess, tolerance, or test equation as needed.
