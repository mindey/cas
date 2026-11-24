# cas

Canonical symbolic-mathematics vocabulary profile for fxy.

Usage:

    import fxy

    fxy.install("mindey/cas")
    fxy.use("mindey/cas")

    x = symbols("x")
    solve(Eq(x**2, 4), x)
    integrate(sp.exp(-x**2), (x, -oo, oo))

The vocabulary provides an explicit SymPy symbolic core as ordinary names,
SymPy itself as sp, and the mpmath context as mp.

For reproducible work, pin a tag or commit:

    fxy.use("mindey/cas@v1")
    fxy.use("mindey/cas@<commit>")

fxy: https://github.com/mindey/fxy
