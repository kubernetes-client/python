# Submodules

To comply with [client library structure requirement](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/csi-client-structure-proposal.md),
python client base utilities is moved into the [kubernetes-client/python-base](https://github.com/kubernetes-client/python-base) repo. `git submodules` is being used to handle dependency to that repo.
This document will provide basic steps to get submodules working.

# Clone repo

To clone the repo, you need to pass the `recursive` parameter to make the clone also get submodules:

```bash
git clone --recursive https://github.com/kubernetes-client/python.git
```

if you have already cloned the repo with no `--recursive` option, you can run this command to get submodules:

```bash
git submodule update --init
```

# Update submodule

If you changed [kubernetes-client/python-base](https://github.com/kubernetes-client/python-base) and want to pull your changes into this repo run this command:

```bash
scripts/update-submodule.sh
```

After the script finishes, please create a commit "generated python-base update" and send a PR to this repository.
