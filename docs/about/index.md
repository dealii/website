About
=======

What is deal.II?
----------------

deal.II — a name that originally meant to indicate that it is the successor to the Differential Equations Analysis Library — is a C++ program library targeted at the computational solution of partial differential equations using adaptive finite elements. It uses state-of-the-art programming techniques to offer you a modern interface to the complex data structures and algorithms required.

The main aim of deal.II is to enable rapid development of modern finite element codes, using among other aspects adaptive meshes and a wide array of tools classes often used in finite element program. Writing such programs is a non-trivial task, and successful programs tend to become very large and complex. We believe that this is best done using a program library that takes care of the details of grid handling and refinement, handling of degrees of freedom, input of meshes and output of results in graphics formats, and the like. Likewise, support for several space dimensions at once is included in a way such that programs can be written independent of the space dimension without unreasonable penalties on run-time and memory consumption.

deal.II is widely used in many academic and commercial projects. For its creation, its principal authors have received the 2007 J. H. Wilkinson Prize for Numerical Software. It is also part of the industry standard SPEC CPU 2006 and SPEC CPU 2017 benchmark suites used to determine the speed of computers and compilers.

deal.II originally emerged from work at the Numerical Methods Group at Universität Heidelberg, Germany, which is at the forefront of adaptive finite element methods and error estimators. Today, it is a global, open source project maintained by a geographically diverse set of developers, and has dozens of contributors and several hundred users scattered around the world. Over the years, development of deal.II has been funded as ancillary products of various grants from the Deutsche Forschungsgemeinschaft, the National Science Foundation, and other funding agencies around the world. We have also received direct funding for particular projects from the Computational Infrastructure in Geodynamics initiative.

What deal.II can offer you
--------------------------

If you are active in the field of adaptive finite element methods, deal.II might be the right library for your projects. Among other features, it offers:

- Support for one, two, and three space dimensions, using a unified interface that allows to write programs almost dimension independent.

- Handling of locally refined grids, including different adaptive refinement strategies based on local error indicators and error estimators. Both h, p, and hp refinement is fully supported for continuous and discontinuous elements.

- Support for a variety of finite elements: Lagrange elements of any order, continuous and discontinuous; Nedelec and Raviart-Thomas elements of any order; elements composed of other elements.

- Parallelization on single machine through the Threading Build Blocks and across nodes via MPI. deal.II has been shown to scale to at least 16k processors.

- Extensive documentation: all documentation is available online in a logical tree structure to allow fast access to the information you need. If printed it comprises more than 500 pages of tutorials, several reports, and presently some 5,000 pages of programming interface documentation with explanations of all classes, functions, and variables. All documentation comes with the library and is available online locally on your computer after installation.

- Modern software techniques that make access to the complex data structures and algorithms as transparent as possible. The use of object oriented programming allows for program structures similar to the structures in mathematical analysis.

- A complete stand-alone linear algebra library including sparse matrices, vectors, Krylov subspace solvers, support for blocked systems, and interface to other packages such as Trilinos, PETSc and METIS.

- Support for several output formats, including many common formats for visualization of scientific data.

- Portable support for a variety of computer platforms and compilers.

- Free source code under an Open Source license, and the invitation to contribute to further development of the library.
