# cas

A small symbolic-mathematics namespace profile for fxy.

Usage with the GitHub-profile branch of fxy:

    import fxy

    fxy.use("mindey/cas")

    x = symbols("x")
    solve(Eq(x**2, 4), x)
    integrate(sp.exp(-x**2), (x, -oo, oo))

For reproducible work, pin this repository by branch, tag, or commit:

    fxy.use("mindey/cas@main")
    fxy.use("mindey/cas@<commit>")

The root fxy.py is declarative: schema metadata plus imports.
Dependency installation remains an explicit approval boundary.
