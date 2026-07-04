# Numeric Methods Collection

This folder contains Python implementations of classic numerical methods used in the coursework labs. Each script is written as a self-contained example runner with worked problems and printed iteration tables.

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

`lab3/` is currently empty.

## Requirements

- Python 3.8 or later
- Standard library only (`math` is the main dependency)

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
- If you want to reuse a method in another program, copy the core function from the corresponding file and import it into your own script.

## Suggested Workflow

1. Open the script for the method you want to study.
2. Review the function definition at the top of the file.
3. Run the file to inspect the iteration trace.
4. Modify the initial guess, tolerance, or test equation as needed.
