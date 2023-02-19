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
import sys

from recommonmark.transform import AutoStructify

# --
# Copy README.md, CONTRIBUTING.md to source/ directory and replace
# all paths to point github files.
def _copy_with_converting_link_to_repo(filename, new_filename):
    base_url = 'https://github.com/kubernetes-client/python/blob/master/'

    def subf(subs):
        label, url = subs.groups()
        if not url.startswith('http://') and not url.startswith('https://'):
            url = base_url + url
        return label + '(' + url + ')'

    with open(filename, "r") as r:
        data = re.sub("(\[[^\]]+\])\(([^\)]+)\)", subf, r.read())

    with open(new_filename, "w") as w:
        w.write(data)

_copy_with_converting_link_to_repo("../../README.md", "README.md")
_copy_with_converting_link_to_repo("../../CONTRIBUTING.md", "CONTRIBUTING.md")
# --

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

