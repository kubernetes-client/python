# This file is intended to document release steps.
# Verify each step's result before calling the next command.
# It is documented here with the intention of being automated
# as a shell script later.

echo 'git clean -xdf'
echo 'python setup.py sdist'
echo 'python setup.py bdist_wheel --universal'
echo 'twine upload dist/* -r https://upload.pypi.org/legacy/ -u kubernetes'

