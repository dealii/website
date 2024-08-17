---
title: Downloads
---

Downloads
======

!!! info

    We provide various options to help you with the installation of deal.II and its dependencies. Please see the [Getting deal.II wiki page](https://github.com/dealii/dealii/wiki/Getting-deal.II) for more information and do not hesitate to ask on the [deal.II discussion group for help](./help.md).


Current Release: 9.6.0
----------------------

Sources |   <span style="font-weight:normal">dealii-9.6.0.tar.gz:  [mirror](/downloads/dealii-9.6.0.tar.gz), [github](https://github.com/dealii/dealii/releases/download/v9.6.0/dealii-9.6.0.tar.gz) <br> (PGP signature file: [mirror](/downloads/dealii-9.6.0.tar.gz.asc), [github]("https://github.com/dealii/dealii/releases/download/v9.6.0/dealii-9.6.0.tar.gz.asc")) <br> August 11, 2024, 39MB. <br> sha256: 675323f0eb8eed2cfc93e2ced07a0ec5727c6a566ff9e7786c01a2ddcde17bed  <br> See [README](/9.6.0/readme.html) for installation instructions or open <code>doc/readme.html</code> after unpacking </span>|
-----------: |:-------------| 
<strong>Offline documentation</strong>      | dealii-9.6.0-offline_documentation.tar.gz: [mirror](/downloads/dealii-9.6.0-offline_documentation.tar.gz), [github](https://github.com/dealii/dealii/releases/download/v9.6.0/dealii-9.6.0-offline_documentation.tar.gz) <br>  (PGP signature file: [mirror](/downloads/dealii-9.6.0-offline_documentation.tar.gz.asc), [github](https://github.com/dealii/dealii/releases/download/v9.6.0/dealii-9.6.0-offline_documentation.tar.gz.asc)) <br>   August 11, 2024, 427MB. <br> sha256:&nbsp;ce83350f58862ebcb06f05955f03532a93695b0f7cffe772ccee2386d12a4e90 | 

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

  <table class="table">
                <tr>
                  <td>
                    <p>
                      <b>
                        Mac OS packages
                      </b>
                    </p>
                  </td>
                  <td>
                    dealii-9.5.0-ventura-intel.dmg, see
                    <a
                      href="/downloads/darwin-images/dealii-9.5.0-ventura-intel.dmg">mirror</a>,
                    <a href="https://github.com/dealii/dealii/releases/download/v9.5.0/dealii-9.5.0-ventura-intel.dmg">github</a>
                    <br/>
                    (PGP signature file:
                    <a href="/downloads/darwin-images/dealii-9.5.0-ventura-intel.dmg.asc">mirror</a>,
                    <a href="https://github.com/dealii/dealii/releases/download/v9.5.0/dealii-9.5.0-ventura-intel.dmg.asc">github</a>)
                    <br/>
                    dealii-9.5.0-ventura-arm64.dmg, see
                    <a
                      href="/downloads/darwin-images/dealii-9.5.0-ventura-arm64.dmg">mirror</a>,
                    <a href="https://github.com/dealii/dealii/releases/download/v9.5.0/dealii-9.5.0-ventura-arm64.dmg">github</a>
                    <br/>
                    (PGP signature file:
                    <a href="/downloads/darwin-images/dealii-9.5.0-ventura-arm64.dmg.asc">mirror</a>,
                    <a href="https://github.com/dealii/dealii/releases/download/v9.5.0/dealii-9.5.0-ventura-arm64.dmg.asc">github</a>)
                    <br/>
                    July 14, 2023, 848MB.
                    <br/>
                    <a href="https://github.com/dealii/dealii/wiki/MacOSX">Mac OSX Instructions</a>
                  </td>
                </tr>

                <tr>
                  <td>
                    <p>
                      <b>Virtual Machine Image</b>
                    </p>
                  </td>
                  <td>
                    <p>
                      An image for virtualbox gives you a complete environment to try out deal.II
                      and works on Mac OS, Linux, and Windows: <br/>
                      <a href="https://www.math.clemson.edu/~heister/dealvm/">More information</a>
                    </p>
                  </td>
                </tr>

                <tr>
                  <td>
                    <p>
                      <b>Dockerized installation</b>
                    </p>
                  </td>
                  <td>
                    <p>
                      Several docker images with full installations of deal.II and (almost) all its dependencies are
                      available on <a href="https://hub.docker.com/r/dealii/dealii/">Docker HUB</a>.
                      These images are guaranteed to work identically on Mac OS, Linux, Windows, on Travis CI, and on gitlab
                      CI. See, for example, the <a href="https://github.com/dealii/dealii/wiki/Docker-Images">
                      Wiki page on Docker-Images</a> to use these images in your own application
                      with Travis CI, gitlab CI, or github actions.
                    </p>
                  </td>
                </tr>

                <tr>
                  <td>
                    <p>
                      <b>Source-based Installers</b>
                    </p>
                  </td>
                  <td>
                    <p>
                      <b><a href="https://github.com/dealii/candi">candi</a></b>
                      is a source based installer for deal.II for various Linux systems that can
                      configure and compile many dependencies for deal.II with minimal effort.
                    </p>
                    <p>
                      deal.II is also distributed in <b><a href="https://spack.io/">Spack</a></b>,
                      a package manager for supercomputers, Linux and Mac OS.
                      With Spack you can build packages with multiple versions, configurations, platforms, and compilers.
                      See the
                      <a href="https://github.com/dealii/dealii/wiki/deal.II-in-Spack">deal.II Spack Wiki page</a> for details.
                    </p>
                  </td>
                </tr>
              </table>


Linux distributions
-----------------

   <table class="table">
                <tr>
                   <td>
                     <p>
                       <b>Arch Linux</b>
                     </p>
                   </td>
                   <td>
                     deal.II is available in the AUR: the snapshot file is
                     available for download
                     <a href="https://aur.archlinux.org/packages/deal-ii/">
                       here</a>.
                   </td>
                </tr>

                <tr>
                  <td>
                    <p>
                      <b>Debian</b>
                    </p>
                  </td>
                  <td>
                    deal.II is available in
                    <a
                      href="https://www.debian.org/releases/testing/">Debian (stretch or newer)</a>.
                    Package information can be found
                    <a href="https://packages.qa.debian.org/d/deal.ii.html">here</a>.
                    Install the development package <code>libdeal.ii-dev</code>.
                    Information about backports of the newest deal.II
                    release is available in <a href="https://backports.debian.org/">here</a>.
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>
                      <b>FreeBSD</b>
                    </p>
                  </td>
                  <td>
                    deal.II is available in
                    <a href="https://www.freshports.org/math/deal.ii">Ports</a>.
                    The package is called <code>deal.ii</code>.
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>
                      <b>Gentoo</b>
                    </p>
                  </td>
                  <td>
                    deal.II is readily packaged in Gentoo. The package is
                    called <code>sci-libs/dealii</code>.
                  </td>
                </tr>
                <tr>
                  <td>
                    <p>
                      <b>Ubuntu</b>
                    </p>
                  </td>
                  <td>
                   <p>
                      deal.II is available in
                      <a href="http://releases.ubuntu.com/yakkety/">Ubuntu LTS 20.04 and newer</a>.
                      Package information can be found <a href="https://launchpad.net/ubuntu/+source/deal.ii">here</a>.
                      Install the development package <code>libdeal.ii-dev</code>.
		      <br>
		      See our <a href="https://github.com/dealii/dealii/wiki/Debian-and-Ubuntu">Debian and Ubuntu Wiki Page</a> for more information.
                    </p>
                   <p>
                      Backports of the deal.II realease to the
                      current stable and lts releases can be obtained here:
                      <a href="https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.5.1-backports">PPA for 9.5.1</a>,
                      <a href="https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.4.0-backports">PPA for 9.4.0</a>,
                      <a href="https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.3.2-backports">PPA for 9.3.2</a>,
                      <a href="https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-9.2.0-backports">PPA for 9.2.0</a>,
                      <a href="https://launchpad.net/~ginggs/+archive/ubuntu/deal.ii-backports">PPA for 9.1.0</a>.
                      Just follow the instructions on how to add the PPA and install the development package
                      <code>libdeal.ii-dev</code> afterwards.
		      <br>
		      See our <a href="https://github.com/dealii/dealii/wiki/Debian-and-Ubuntu">Debian and Ubuntu Wiki Page</a> for more information.
                    </p>
                  </td>
                </tr>
              </table>


|

