# Submodules
To comply with [client library structure requirement](https://github.com/kubernetes-client/community/blob/master/design-docs/clients-library-structure.md),
python client base utilities is moved into kubernetes-client/python-base repo. `git submodules` is being used to handle dependency to that repo.
This document will provide basic steps to get submodules work.

# Clone repo
To clone repo, you need to pass `recursive` parameter to make the clone also get submodules:

```bash
git clone --recursive https://github.com/kubernetes-client/python.git
```

if you already clone repo with no `--recursive` option, you can run this command to get submodules:

```bash
git submodule update --init
```

# Update submodule
If you changed kubernetes-client/python-base and want to pull your changes into this repo run this command:

```bash
git submodule update --remote
```

Once updated, you should create a new PR to commit changes to the repository.

