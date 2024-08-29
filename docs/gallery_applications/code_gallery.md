Code Gallery
=============

The deal.II "code gallery" is an extension to the deal.II tutorial. 
While the tutorial's emphasis is on teaching aspects of deal.II by providing concrete examples — 
and extensive documentation and discussion — 
of how parts of deal.II are used in applications, 
the intent of the code gallery is to *provide starting points* for your own codes 
by making available codes others have already written. 

As a general rule:

* The code gallery is not part of deal.II. 
  The applications in the code gallery were written by users 
  who wanted to make their codes available
* The applications in the code gallery are generally 
  not as well tested or documented as the tutorial programs.
  **These codes come with no warranty at all**.
  If you have questions, you need to contact the authors of these codes, not the authors of deal.II
* **We welcome additions and improvements to existing codes, 
  as well as new code gallery applications!** 
  Most users start their own applications from an existing tutorial program.
  Having more starting points helps others, 
  but it also gives code gallery authors additional ways to get recognition for their own codes! 
  See [the code gallery repository](https://github.com/dealii/code-gallery) for instructions on how to contribute.


  <div class="grid" markdown>
  
  [:octicons-image-16: Codes](https://dealii.org/developer/doxygen/deal.II/CodeGallery.html){ .md-button .md-button--primary .center }<br>
  See the list of programs that are part of the code gallery. 
  { .card }
  
  [:octicons-download-16: Download](#downloading-the-code-gallery){ .md-button .md-button--primary .center }<br>
  Downloading the programs of the code gallery is easy. 
  { .card }
  
  [:fontawesome-solid-paper-plane: Contribute](https://github.com/dealii/code-gallery){ .md-button .md-button--primary .center }<br>
  Contribute your own codes as a starting point for others. 
  { .card }
  
  
  </div>


Downloading the code gallery
----------------------------

You can get the entire code gallery from its GitHub home by using the command 

```
git clone https://github.com/dealii/code-gallery.git
```

This creates a directory `code-gallery/` that contains all gallery programs.

If you want to generate the deal.II documentation locally
and want it also to cross-link to the code galery, you need to do the step above withing your copy of deal.II, 
i.e., so that the command above creates a directory `code-gallery/`
parallel to the `include/`, `source/` and `/examples` (and other) directories.