---
title: deal.II
---
#

!!! note ""

    <b>What it is</b>: A C++ software library supporting the creation of finite element codes and an open community of users and developers. ([About deal.II](about/index.md))

    <b>Mission</b>: To provide well-documented tools to build finite element codes for a broad variety of PDEs, from laptops to supercomputers. ([deal.II documentation](https://dealii.org/current/doxygen/deal.II))

    <b>Vision</b>: To create an open, inclusive, participatory community providing users and developers with a state-of-the-art, comprehensive software library that constitutes the go-to solution for all finite element problems. ([Participate in deal.II](community/index.md))


<div class="grid" markdown>

[:octicons-download-16: Download](current_release/download.md){ .md-button .md-button--primary .center }<br>
deal.II is open source and available for free!
{ .card }

[:fontawesome-solid-book: Documentation](https://dealii.org/current/doxygen/deal.II){ .md-button .md-button--primary .center }<br>
deal.II has extensive documentation and tutorials!
{ .card }

[:fontawesome-solid-paper-plane: Participate](community/index.md){ .md-button .md-button--primary .center }<br>
deal.II is a community project and welcomes participation!
{ .card }

[:material-help: Help](getting_help/index.md){ .md-button .md-button--primary .center }<br>
deal.II provides resources to learn and ask for help!
{ .card }

</div>

News
----

- 2026/08/09: **Version 9.8.0 released**:
deal.II version 9.8.0 was released today. A full list of changes can be found [here](https://dealii.org/developer/doxygen/deal.II/changes_between_9_7_1_and_9_8_0.html) and a long description of changes is in the manuscript [here](https://dealii.org/deal98-preprint.pdf). Download links are on the [download](current_release/download.md) page, or the [release page on github](https://github.com/dealii/dealii/releases).

- 2026/05/11: New tutorial programs [step-98](https://dealii.org/developer/doxygen/deal.II/step_98.html)
and [step-100](https://dealii.org/developer/doxygen/deal.II/step_100.html): step-98 shows
how to solve two-dimensional magnetostatic curl-curl problems, and step-100 applies a
discontinuous Petrov-Galerkin method to the time-harmonic Helmholtz equation.
There are also several new code gallery programs:
[Parallel implementation of heat equation](https://dealii.org/developer/doxygen/deal.II/code_gallery_Heat_Eqn_Parallel.html),
a transient heat equation solver with adaptive mesh refinement and a parallel solver;
[L-BFGS phasefield solver](https://dealii.org/developer/doxygen/deal.II/code_gallery_L_BFGS_phasefield_solver.html),
a limited-memory BFGS monolithic solver for phase-field crack simulations;
[An agglomeration-based solver for the Poisson problem](https://dealii.org/developer/doxygen/deal.II/code_gallery_agglomeration_poisson.html),
a discontinuous Galerkin solver for the Poisson problem on general polytopal meshes generated
through mesh agglomeration;
[An ALE approach for large-deformation thermoplasticity](https://dealii.org/developer/doxygen/deal.II/code_gallery_ALE_Finite_Strain_Plasticity.html),
an implementation of a large-deformation arbitrary Lagrangian-Eulerian finite-strain thermoplasticity solver;
[Parallel flow routing](https://dealii.org/developer/doxygen/deal.II/code_gallery_parallel_flow_routing.html),
a parallel solver for determining how much water is available at every point of a landscape;
[Parallel Vibroacoustic Solver](https://dealii.org/developer/doxygen/deal.II/code_gallery_Parallel_Vibro_Acoustic_Solver.html),
a parallel frequency-domain vibroacoustic solver calculating the sound transmission loss of a concrete wall;
and [Multilevel Monte Carlo for random Darcy flow](https://dealii.org/developer/doxygen/deal.II/code_gallery_MLMC_random_darcy_flow.html),
an implementation of a multilevel Monte Carlo method for random Darcy flow.

- 2025/10/14: We wrote an editorial in SIAM News about mathematical software:
[Supporting computational science and engineering: How widely-used software in industrial and applied mathematics is created](https://www.siam.org/publications/siam-news/articles/supporting-computational-science-and-engineering-the-creation-of-widely-used-software-in-industrial-and-applied-mathematics/)
[(pdf version)](large_assets/miscellaneous/20251014-siam_news.pdf).

- 2025/09/30: [Best deal.II-based paper of 2024: D. Abbondanza, M. Gallo, C. M. Casciola:
"Collapse of microbubbles over an elastoplastic wall"](community/best_paper_award.md).

[(older news)](about/news.md)

Videos
------

<div id="video-timeline"></div>
<script>
  const timelineSource = "1FYT2_aIxZT4VFJeJDrqAu5out9HwCDwsxWU299e5hlk";
  const timelineContainer = document.getElementById("video-timeline");

  function addTimeline(initialSlide) {
    const timeline = document.createElement("iframe");
    timeline.src =
      "https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=" +
      timelineSource +
      "&font=Default&lang=en&initial_zoom=2&height=650&start_at_slide=" +
      initialSlide;
    timeline.width = "100%";
    timeline.height = "650";
    timeline.setAttribute("webkitallowfullscreen", "");
    timeline.setAttribute("mozallowfullscreen", "");
    timeline.setAttribute("allowfullscreen", "");
    timeline.frameBorder = "0";
    timelineContainer.appendChild(timeline);
  }

  fetch("https://docs.google.com/spreadsheets/d/" + timelineSource + "/pub?output=csv")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Unable to retrieve the video timeline.");
      }
      return response.text();
    })
    .then((csv) => {
      const entries = csv.trim().split(/\r?\n/).length - 1;
      if (entries < 1) {
        throw new Error("The video timeline does not contain any entries.");
      }
      addTimeline(Math.floor(Math.random() * entries));
    })
    .catch((error) => {
      console.error(error);
      addTimeline(0);
    });
</script>
`
