# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'lims_portal'
copyright = '2024, Abhay'
author = 'Abhay'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# Check if we are running on Read the Docs
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# If building on Read the Docs, override the output directory
if on_rtd:
    html_output = os.environ.get('READTHEDOCS_OUTPUT', '_build')
else:
    html_output = '_build'

# Ensure that the output directory is set correctly
html_output = os.path.join(html_output, 'html')
