---
title: Home
---

ryujin
======

<b>ryujin</b> is a high-performance high-order collocation-type
finite-element solver for conservation equations such as the compressible
Navier-Stokes and Euler equations of gas dynamics. The solver is based on
the [convex limiting technique](https://doi.org/10.1137/17M1149961) to
ensure [invariant domain preservation](https://doi.org/10.1137/16M1074291)
and uses the finite element library
[deal.II](https://github.com/dealii/dealii)
([website](https://www.dealii.org)) and the [vector class SIMD
library](https://github.com/vectorclass/version2). As such the solver
maintains important physical invariants and is guaranteed to be stable
without the use of ad-hoc tuning parameters.

Features
--------


Modules
-------

Ryujin features the following equation modules selectable by the following
parameter flags:

 - `equation = euler`, an optimized solver module for the
   [compressible Euler
   equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics))
   with polytropic equation of state.
 - `equation = euler aeos`, a generalized solver module for the
   compressible Euler equation with an [arbitrary or tabulated equation of
   state](https://en.wikipedia.org/wiki/Equation_of_state).
 - `equation = navier stokes`, an optimized solver module for the
   [compressible Navier-Stokes
   equations](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations)
   with polytropic equation of state,
   Newtonian fluid model, and Fourier's law for the heat flux.
 - `equation = shallow water`, a module for the [shallow-water
   equations](https://en.wikipedia.org/wiki/Shallow_water_equations).
 - `equation = scalar conservation`, a module for scalar conservation
   equations with user-supplied flux. The module features a greedy
   wave-speed estimate to maintain an invariant domain, a generic indicator
   based on the entropy-viscosity commutator technique with a general,
   entropy-like function, and a customizable convex limiter.
