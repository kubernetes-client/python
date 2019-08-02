# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import shutil
import sys

from recommonmark.transform import AutoStructify

# Work around https://github.com/readthedocs/recommonmark/issues/152
new_readme = []

with open("../../README.md", "r") as r:
    lines = r.readlines()
    for l in lines:
        nl = re.sub("\[!\[[\w\s]+\]\(", "[![](", l)
        new_readme.append(nl)

with open("README.md", "w") as n:
    n.writelines(new_readme)

# apparently index.rst can't search for markdown not in the same directory
shutil.copy("../../CONTRIBUTING.md", ".")

sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ----------------------------------------------------

source_suffix = ['.rst', '.md']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx_markdown_tables',
    'recommonmark',
    'sphinx.ext.autodoc',
    #'sphinx.ext.intersphinx',
]

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'kubernetes-python-client'
copyright = u'2017, Kubernetes'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
# html_static_path = ['static']

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     '%s.tex' % project,
     u'%s Documentation' % project,
     u'Kubernetes', 'manual'),
]

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}
def setup(app):
    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
            }, True)
    app.add_transform(AutoStructify)

