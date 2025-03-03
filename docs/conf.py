# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
project = "aioopenexchangerates"
project_copyright = "2024, Martin Hjelmare"
author = "Martin Hjelmare"
release = "0.6.21"

# General configuration
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
]

# The suffix of source filenames.
source_suffix = [
    ".rst",
    ".md",
]
templates_path = [
    "_templates",
]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
