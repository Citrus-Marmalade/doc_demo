##################################
Welcome to My Sphinx Documentation
##################################
This project sets up a Sphinx documentation site using RestructureText for the source files and the Furo theme for styling.


Example of docs
=================
.. card-carousel:: 2

   .. card::
      :link: sphinx-demo
      :link-type: ref
      :text-align: center

      :octicon:`code-square;2em;sd-text-info` 

      sphinx-demo


   .. card:: 
      :link: nxp-port
      :link-type: ref
      :text-align: center

      :octicon:`file;2em;sd-text-info`

      NXP Port Documentation 
         

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   sphinx_demo
   nxp_port/doc
   versioned/doc