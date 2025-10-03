---
title: Downloads
---

Downloads
======

!!! info

    We provide various options to help you with the installation of deal.II and its dependencies. Please see the [Getting deal.II wiki page](https://github.com/dealii/dealii/wiki/Getting-deal.II) for more information and do not hesitate to ask on the [deal.II discussion group for help](../getting_help/index.md).


Current Release: 9.7.1
----------------------

Sources |   <span style="font-weight:normal">dealii-9.7.1.tar.gz:  [mirror](/downloads/dealii-9.7.1.tar.gz), [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1.tar.gz) <br> (PGP signature file: [mirror](/downloads/dealii-9.7.1.tar.gz.asc), [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1.tar.gz.asc)) <br> September 14, 2025, 41MB. <br> sha256:&nbsp;0f2096ef83db54fdcebe9f3d148fa713f63f1c3f567941b53bcb4a1a8ea7de43<br> See [README](/9.7.0/readme.html) for installation instructions or open <code>doc/readme.html</code> after unpacking </span>|
-----------: |:-------------|
<strong>Offline documentation</strong>      | dealii-9.7.0-offline_documentation.tar.gz: [mirror](/downloads/dealii-9.7.0-offline_documentation.tar.gz), [github](https://github.com/dealii/dealii/releases/download/v9.7.0/dealii-9.7.0-offline_documentation.tar.gz) <br>  (PGP signature file: [mirror](/downloads/dealii-9.7.0-offline_documentation.tar.gz.asc), [github](https://github.com/dealii/dealii/releases/download/v9.7.0/dealii-9.7.0-offline_documentation.tar.gz.asc)) <br>   July 22, 2025, 448MB. <br> sha256:&nbsp;93fdfa3ea7a64a803ab7ba0dc3bc89b2708c5348ccb621d42d766e7fb67aa865 |

Previous versions
-----------------

  Older deal.II releases can be found on the
                <a href="https://github.com/dealii/dealii/releases">Github release page</a>,
                or on the
                <a href="/downloads/">mirror</a>.


Development sources
-------------------

 To stay in sync with the most recent development version,
                have a look at our
                <a href="https://github.com/dealii/dealii">git repository</a>
                hosted on github. This provides the latest features (as well
                as the latest bugs.)
                You can clone the repository directly on the command line via
```
  git clone https://github.com/dealii/dealii.git
```
 Contributing to the deal.II development is easy and is best done
                by forking the deal.II repository. To do this, create an account
                on github and then, when you're logged in, click on the "Fork"
                button at the top right
                of <a href="https://github.com/dealii/dealii">the deal.II github
                page</a>. There are good tutorials on how to contribute to
                projects at <a href="https://github.com/">github's front
                page</a>. An introduction to how git works can be found
                <a href="https://www.atlassian.com/git/tutorial">here</a>
        or <a href="https://marklodato.github.io/visual-git-guide/index-en.html">here</a>.
              </p>


Installers and images
---------------------

| **Mac OS packages**        |  dealii-9.7.1-sequoia-arm64-clang17.dmg, see [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1-sequoia-arm64-clang17.dmg)  <br>  (PGP signature file: [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1-sequoia-arm64-clang17.dmg.asc)) <br> September 19, 2025, 1.03GB.  <br>  [Mac OSX Instructions](https://github.com/dealii/dealii/wiki/MacOSX) |
|                            |  dealii-9.7.1-tahoe-arm64-clang17.dmg, see [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1-tahoe-arm64-clang17.dmg)  <br>  (PGP signature file: [github](https://github.com/dealii/dealii/releases/download/v9.7.1/dealii-9.7.1-tahoe-arm64-clang17.dmg.asc)) <br> September 19, 2025, 1.03GB.  <br>  [Mac OSX Instructions](https://github.com/dealii/dealii/wiki/MacOSX) |
-----------: |:-------------|
| **Virtual Machine Image**   | An image for VirtualBox gives you a complete environment to try out deal.II and works on Mac OS, Linux, and Windows:   <br> [More information](https://www.math.clemson.edu/~heister/dealvm/)                                                                                                                 |
| **Dockerized installation** | Several Docker images with full installations of deal.II and (almost) all its dependencies are available on [Docker HUB](https://hub.docker.com/r/dealii/dealii/).  These images are guaranteed to work identically on Mac OS, Linux, Windows, on Travis CI, and on GitLab CI.  See, for example, the [Wiki page on Docker-Images](https://github.com/dealii/dealii/wiki/Docker-Images) to use these images in your own application with Travis CI, GitLab CI, or GitHub Actions. |
| **Source-based Installers** | **[candi](https://github.com/dealii/candi)** is a source-based installer for deal.II for various Linux systems that can configure and compile many dependencies for deal.II with minimal effort.  deal.II is also distributed in **[Spack](https://spack.io/)**, a package manager for supercomputers, Linux, and Mac OS.  With Spack, you can build packages with multiple versions, configurations, platforms, and compilers.  See the [deal.II Spack Wiki page](https://github.com/dealii/dealii/wiki/deal.II-in-Spack) for details. |



Linux distributions
-----------------

| **Arch Linux**  | deal.II is available in the AUR: the snapshot file is available for download [here](https://aur.archlinux.org/packages/deal-ii/). |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Debian**      | deal.II is available in [Debian (stretch or newer)](https://www.debian.org/releases/testing/).<br>Package information can be found [here](https://packages.qa.debian.org/d/deal.ii.html).<br>Install the development package `libdeal.ii-dev`.<br>Information about backports of the newest deal.II release is available [here](https://backports.debian.org/). |
| **FreeBSD**     | deal.II is available in [Ports](https://www.freshports.org/math/deal.ii).<br>The package is called `deal.ii`. |
| **Gentoo**      | deal.II is readily packaged in Gentoo.<br>The package is called `sci-libs/dealii`. |
| **Ubuntu**      | deal.II is available in [Ubuntu LTS 20.04 and newer](http://releases.ubuntu.com/yakkety/).<br>Package information can be found [here](https://launchpad.net/ubuntu/+source/deal.ii).<br>Install the development package `libdeal.ii-dev`.<br>See our [Debian and Ubuntu Wiki Page](https://github.com/dealii/dealii/wiki/Debian-and-Ubuntu) for more information.<br><br>Backports of the deal.II release to the current stable and LTS releases can be obtained here:<br>- [PPA for 9.6.0](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.6.0-backports)<br>- [PPA for 9.5.1](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.5.1-backports)<br>- [PPA for 9.4.0](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.4.0-backports)<br>- [PPA for 9.3.2](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.3.2-backports)<br>- [PPA for 9.2.0](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.2.0-backports)<br>- [PPA for 9.1.0](https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-backports)<br>Just follow the instructions on how to add the PPA and install the development package `libdeal.ii-dev` afterwards.<br>See our [Debian and Ubuntu Wiki Page](https://github.com/dealii/dealii/wiki/Debian-and-Ubuntu) for more information. |
