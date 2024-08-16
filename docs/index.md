---
title: Home
---

deal.II - an open source finite element library
======

<b>What it is</b>: A C++ software library supporting the creation of finite element codes and an open community of users and developers. (Learn more.)

<b>Mission</b>: To provide well-documented tools to build finite element codes for a broad variety of PDEs, from laptops to supercomputers.

<b>Vision</b>: To create an open, inclusive, participatory community providing users and developers with a state-of-the-art, comprehensive software library that constitutes the go-to solution for all finite element problems.



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
