# Release process

The release process of the python client involves creating (or updating) a release
branch, updating release tags, and creating distribution packages and uploading them to
pypi.

## Hot issues

There are some hot issues with the client generation that require manual fixes.
***The steps in this section should be performed after you finished the section "Update release tags".***

1. Restore custom object patch hehavior. You should apply [this commit](https://github.com/kubernetes-client/python/pull/995/commits/9959273625b999ae9a8f0679c4def2ee7d699ede)
to ensure custom object patch behavior is backwards compatible. For more
details, see [#866](https://github.com/kubernetes-client/python/issues/866) and
[#959](https://github.com/kubernetes-client/python/pull/959).

2. Add alias package kubernetes.client.apis with deprecation warning. You need
to add [this file](https://github.com/kubernetes-client/python/blob/0976d59d6ff206f2f428cabc7a6b7b1144843b2a/kubernetes/client/apis/__init__.py)
under `kubernetes/client/apis/` to ensure the package is backwards compatible.
For more details, see [#974](https://github.com/kubernetes-client/python/issues/974)

3. Add ability to the client to be used as Context Manager [kubernetes-client/python#1073](https://github.com/kubernetes-client/python/pull/1073)

Commit the manual changes like this [PR](https://github.com/kubernetes-client/python/pull/995/commits) does,
then create your PR for review.

Alternatively, you can use the `scripts/apply-hotfixes.sh` script to apply changes from the above functionalities. **As mentioned above the script should be run after finishing the section `Update release tags`. Also, ensure a clean working directory before applying the script**

## Change logs
Make sure the change logs are up to date [here](https://github.com/kubernetes-client/python/blob/master/CHANGELOG.md).
If they are not, follow commits added after the last release and update/commit
the change logs to master.

Then based on the release, follow one of next two steps.

## Update pre-release branch

The release branch name should have release-x.x format. All minor and pre-releases
should be on the same branch. To update an existing branch with master (only for
latest pre-release):

```bash
export RELEASE_BRANCH=release-x.y
git checkout $RELEASE_BRANCH
git fetch upstream
git rebase upstream/$RELEASE_BRANCH
git pull upstream master
```

You may need to fix some conflicts. For auto-generated files, you can commit
either version. They will be updated to the current version in the next step.

## Patch a release branch

If you are releasing a patch to an existing stable release, you should do a
cherry pick first:

```bash
scripts/cherry_pick_pull.sh
```

Do not merge master into a stable release branch. Run the script without
parameters and follow its instructions to create a cherry pick PR. Get the
PR merged then update your local branch:

```bash
export RELEASE_BRANCH=release-x.y
git checkout $RELEASE_BRANCH
git fetch upstream
git rebase upstream/$RELEASE_BRANCH
```

## Sanity check generated client

We need to make sure there are no API changes after running update client
scripts. Such changes should be committed to the master branch first. Run this
command:

```bash
scripts/update-client.sh
```

And make sure there is no API change (version number changes should be fine
as they will be updated in the next step anyway). Do not commit any changes at
this step and go back to the master branch if there are any API changes.

## Update release tags

Release tags are in the "scripts/constants.py" file. These are the constants you may
need to update:

CLIENT_VERSION: Client version should follow x.y.zDn where x,y,z are version
numbers (integers) and D is one of "a" for alpha or "b" for beta and n is the
pre-release number. For a final release, the "Dn" part should be omitted. Examples:
1.0.0a1, 2.0.1b2, 1.5.1.

DEVELOPMENT_STATUS: Update it to one of the values of "Development Status"
in [this list](https://pypi.python.org/pypi?%3Aaction=list_classifiers).

after changing constants to proper versions, update the client using this
command:

```bash
scripts/update-client.sh
```

and commit changes (should be only version number changes) to the release branch.
Name the commit something like "Update version constants for XXX release".

***After you finished the steps above, refer to the section "Hot issues" and
apply the manual fixes.***

```bash
git push upstream $RELEASE_BRANCH
```

## Make distribution packages

First make sure you are using a clean version of python. Use virtualenv and
pyenv packages. Make sure you are using python 2.7.12. I would normally do this
on a clean machine:

(install [pyenv](https://github.com/yyuu/pyenv#installation))
(install [pip](https://pip.pypa.io/en/stable/installing/))
(install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/))

```bash
git clean -xdf
pyenv install -s 2.7.12
pyenv global 2.7.12
virtualenv .release
source .release/bin/activate
python --version     # Make sure you get Python 2.7.12
pip install twine
```

Now we need to create a "~/.pypirc" with this content:

```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = kubernetes
```

TODO: we should be able to pass these parameters to twine directly. My first attempt failed.

Now that the environment is ready, lets create distribution packages:

```bash
python setup.py sdist
python setup.py bdist_wheel --universal
ls dist/
```

You should see two files in dist folder: "kubernetes\*.whl" and "kubernetes\*.tar.gz".

TODO: We need a dry-run option and some way to test the package upload process to pypi.

If everything looks good, run this command to upload packages to pypi:

```
twine upload dist/*
```

## Create github release

Create a gihub release by starting from
[this page](https://github.com/kubernetes-client/python/releases).
Click the `Draft a new release button`. Name the tag the same as CLIENT_VERSION. Change
the target branch to "release-x.y". If the release is a pre-release, check the
`This is a pre-release` option.

## Announcement

Send an announcement email to kubernetes-dev@googlegroups.com with the subject: [ANNOUNCE] kubernetes python-client $VERSION is released

## Cleanup

```bash
deactivate
rm -rf .release
```

TODO: Convert steps in this document to an (semi-) automated script.

ref: https://packaging.python.org/distributing/
