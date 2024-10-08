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
    'sphinxcontrib.openapi',
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

import os
import sys

# Add the lims_portal folder to the Python path
sys.path.insert(0, os.path.abspath('..'))  # Go up one level from sphinx/ to lims_portal/
os.environ['DJANGO_SETTINGS_MODULE'] = 'lims_portal.settings'  # Use the correct settings file

# Initialize Django
import django
django.setup()




html_output = os.environ.get('READTHEDOCS_OUTPUT', '_build')


