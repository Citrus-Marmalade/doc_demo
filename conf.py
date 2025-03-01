# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'CPC'
author = 'Cirtus-Marmalade'
release = 'Demo'

# General configuration
extensions = [
    'sphinx_design'
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'furo'
html_static_path = ['_static']

html_logo = '_static/logo.png'