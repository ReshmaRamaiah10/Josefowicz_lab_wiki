# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Josefowicz_Lab'
copyright = '2024, Reshma'
author = 'Reshma Ramaiah'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'myst_parser',  # For Markdown support
    'jupyter_sphinx',  # For Jupyter Notebooks
]

# Optionally, configure myst-parser options
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "linkify",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Add a custom option for the edit link
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'nav_links': [
        {
            'name': 'Edit on Github',
            'url': 'https://github.com/ReshmaRamaiah10/Josefowicz_lab_wiki/blob/main/docs/source/index.rst',
            'newtab': True,
        },
    ],
}

