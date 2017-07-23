# python-base

[![Build Status](https://travis-ci.org/kubernetes-client/python-base.svg?branch=master)](https://travis-ci.org/kubernetes-client/python-base)

This is the utility part of the [python client](https://github.com/kubernetes-incubator/client-python). It has been added to the main
repo using git submodules. This structure allow other developers to create
their own kubernetes client and still use standard kubernetes python utilities.
For more information refer to [clients-library-structure](https://github.com/kubernetes-client/community/blob/master/design-docs/clients-library-structure.md).

# Development
Any changes to utilites in this repo should be send as a PR to this repo. After
the PR is merged, developers should create another PR in the main repo to update
the submodule. See [this document](https://github.com/kubernetes-incubator/client-python/blob/master/devel/submodules.md) for more guidelines.
