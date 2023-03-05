# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXAPIDOC  = sphinx-apidoc
SPHINXOPTS    = -c source
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = kubernetes-python
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# additional step to use sphinx-apidoc to generate rst files for APIs
rst:
	rm -f $(SOURCEDIR)/kubernetes.*.rst
	$(SPHINXAPIDOC) -o "$(SOURCEDIR)" ../kubernetes/ -e -f

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
html: rst
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "\nDocs rendered successfully, open _/build/html/index.html to view"
