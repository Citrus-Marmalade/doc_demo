# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'CPC Documentation Demo'
author = 'Cirtus-Marmalade'
release = '0.1'

# General configuration
extensions = [
    'myst_parser',  # For Markdown support
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'furo'
html_static_path = ['_static']

html_logo = '_static/logo.png'