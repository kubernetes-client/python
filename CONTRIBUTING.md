# Contributing

Thanks for taking the time to join our community and start contributing!

Any changes to utilities in this repo should be send as a PR to this repo.
After the PR is merged, developers should create another PR in the main repo to update the submodule.
See [this document](https://github.com/kubernetes-client/python/blob/master/devel/submodules.md) for more guidelines.

The [Contributor Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/README.md)
provides detailed instructions on how to get your ideas and bug fixes seen and accepted.

Please remember to sign the [CNCF CLA](https://github.com/kubernetes/community/blob/master/CLA.md) and
read and observe the [Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

## Adding new Python modules or Python scripts
If you add a new Python module please make sure it includes the correct header
as found in:
```
hack/boilerplate/boilerplate.py.txt
```

This module should not include a shebang line.

If you add a new Python helper script intended for developers usage, it should
go into the directory `hack` and include a shebang line `#!/usr/bin/env python`
at the top in addition to rest of the boilerplate text as in all other modules.

In addition this script's name should be added to the list   
`SKIP_FILES`  at the top of hack/boilerplate/boilerplate.py.
