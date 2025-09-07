import os
import sys
import datetime

sys.path.insert(0, os.path.abspath('..'))

project = "anilibria-api-client"
copyright = f'{datetime.datetime.now().year}, semen-bol'
author = "semen-bol"
release = "0.1.5"
version = "0.1"

add_module_names = False
autodoc_typehints = "description"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_default_options = {
    "member-order": "bysource",
    "members": True,
    "show-inheritance": True,
    "undoc-members": True,
    "special-members": "__init__",
}

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'titles_only': False
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
}

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True