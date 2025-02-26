===========
Sphinx Demo
===========

.. _sphinx-demo:

Project Structure
=================

.. parsed-literal::

   doc_demo
   ├── _static          # Custom static files (CSS, JS)
   ├── _templates       # Custom templates for documentation layout
   ├── docs/            # Build output for the generated HTML documenation.
   ├── conf.py          # Sphinx configuration file
   ├── index.md         # Main entry point for the documentation
   ├── nxp_port         # NXP port documenation folder/
   │   └──doc.rst       # Getting started with NXP port source file.
   ├── requirements.txt # Required Python package
   └── doc_gen.py       # Python script to generate the documentation.


Getting Started
===============

To set up the Sphinx documentation project, follow these steps:

1. **Install Requirements**: Make sure you have Python installed, then install the required packages by running:
   .. parsed-literal::

      pip install -r docs/requirements.txt


2. **Build the Documentation**: Navigate to the `docs` directory and run:
   .. parsed-literal::

      sphinx-build -b html . docs

    

3. **View the Documentation**: Open the generated HTML files in the `docs/` directory in your web browser.

Customization
=============

- You can add custom static files (like CSS or JavaScript) in the `docs/_static` directory.
- If you want to modify the layout, create custom templates in the `docs/_templates` directory.
- Update the `docs/conf.py` file to configure Sphinx settings and extensions.

Extensions Example
------------------

1. `Furo theme <https://sphinx-themes.org/sample-sites/furo/kitchen-sink/>`_
2. `Sphinx-Design <https://sphinx-design.readthedocs.io/en/furo-theme/>`_

License
=======

This project is licensed under the MIT License. See the LICENSE file for more details.
