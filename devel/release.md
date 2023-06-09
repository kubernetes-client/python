# Release process

The release process for the python client involves creating (or updating) a
release branch, updating release tags, and creating distribution packages and
uploading them to pypi.

There are several releases per version:
- snapshot
- a1 (alpha release)
- b1 (beta release)
- final release

Between each release, there is a waiting period of about two weeks for users to
report issues. Typically, there is a single alpha or beta release, but if there
are a higher than expected number of issues there can be multiple releases
(e.g, a2 or b2).

## Automated release

### 1. Run the release script and send a PR
Generate a Github personal access token following instruction
[link](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

```
export GITHUB_TOKEN=t  # github-personal-access-token
export MINOR_VERSION=x
export PATCH_VERSION=y  # The latest patch version for the minor version. Not required for snapshot.
```
To create a snapshot:
```
$ KUBERNETES_BRANCH=release-1.${MINOR_VERSION} CLIENT_VERSION=${MINOR_VERSION}.0.0+snapshot DEVELOPMENT_STATUS="3 - Alpha" scripts/release.sh
```
To create an a1 release:
```
$ KUBERNETES_BRANCH=release-1.${MINOR_VERSION} CLIENT_VERSION=${MINOR_VERSION}.${PATCH_VERSION}.0a1 DEVELOPMENT_STATUS="3 - Alpha" scripts/release.sh
```
To create a b1 release:
```
$ KUBERNETES_BRANCH=release-1.${MINOR_VERSION} CLIENT_VERSION=${MINOR_VERSION}.${PATCH_VERSION}.0b1 DEVELOPMENT_STATUS="4 - Beta" scripts/release.sh
```
To create a stable release:
```
$ KUBERNETES_BRANCH=release-1.${MINOR_VERSION} CLIENT_VERSION=${MINOR_VERSION}.${PATCH_VERSION}.0 DEVELOPMENT_STATUS="5 - Production/Stable" scripts/release.sh
```
Checkout the generated local branch (named "automated-release-of-xxx") to
continue with the remaining steps.

### 2. README (not required for snapshots)

Update the compatibility matrix and maintenance status in the README file.

### 3. Submit pull request

For snapshots, create a PR against the master repo.

For actual releases, create:
- a PR against the release branch
- a second PR against the master branch to cherrypick the CHANGELOG and README
  changes.

### 4. (Repo admin) Create release branch

After merging a new snapshot, create a release branch from the master branch.

## (Deprecated) Manual release

### 1. Create or update release branch

The release branch name should have release-x.x format. All minor and pre-releases
should be on the same branch. To update an existing branch with master (only for
latest pre-release):

```bash
export RELEASE_BRANCH=release-x.y
git checkout $RELEASE_BRANCH
git fetch upstream
git rebase upstream/$RELEASE_BRANCH
git pull -X theirs upstream master
```

You may need to fix some conflicts. For auto-generated files, you can commit
either version. They will be updated to the current version in the next step.

### 2. Update release tags

Release tags are in the "scripts/constants.py" file. These are the constants you
may need to update:

CLIENT_VERSION: Client version should follow x.y.zDn where x,y,z are version
numbers (integers) and D is one of "a" for alpha or "b" for beta and n is the
pre-release number. For a final release, the "Dn" part should be omitted.
Examples:
- 1.0.0a1 (alpha release)
- 2.0.1b2 (beta release)
- 1.5.1 (final release)

DEVELOPMENT_STATUS: Update it to one of the values of "Development Status" in
[this list](https://pypi.python.org/pypi?%3Aaction=list_classifiers).

After changing constants to proper versions, update the client using this
command:

```bash
scripts/update-client.sh
```

**NOTE**: If you see a lot of new or modified files under the `kubernetes/test/`
directory, delete everything except `kubernetes/test/test_api_client.py` and
`kubernetes/test/test_configuration.py`.

Commit changes (should be only version number changes) to the release branch.
Name the commit something like "Update version constants for XXX release".

***After you finished the steps above, refer to the section, "Hot issues", and
apply the manual fixes.***

```bash
git push upstream $RELEASE_BRANCH
```

### 3. Hot issues

Use the `scripts/apply-hotfixes.sh` script to apply the fixes below in one step.
**As mentioned above, the script should be run after finishing the section "Update release tags". Also, ensure a clean working directory before applying the script.**

Commit the manual changes like this [PR](https://github.com/kubernetes-client/python/pull/995/commits) does.

There are some hot issues with the client generation that require manual fixes.
**The steps below are deprecated and only exist for documentation purposess. They should be performed using the `scripts/apply-hotfixes.sh` script mentioned above.**

1. Restore custom object patch behavior. You should apply [this commit](https://github.com/kubernetes-client/python/pull/995/commits/9959273625b999ae9a8f0679c4def2ee7d699ede)
to ensure custom object patch behavior is backwards compatible. For more
details, see [#866](https://github.com/kubernetes-client/python/issues/866) and
[#959](https://github.com/kubernetes-client/python/pull/959).

2. Add alias package kubernetes.client.apis with deprecation warning. You need
to add [this file](https://github.com/kubernetes-client/python/blob/0976d59d6ff206f2f428cabc7a6b7b1144843b2a/kubernetes/client/apis/__init__.py)
under `kubernetes/client/apis/` to ensure the package is backwards compatible.
For more details, see [#974](https://github.com/kubernetes-client/python/issues/974)

3. Add ability to the client to be used as Context Manager [kubernetes-client/python#1073](https://github.com/kubernetes-client/python/pull/1073)

4. Remove the tests directory (ref: https://github.com/kubernetes-client/python/commit/ec9c944f076999543cd2122aff2d86f969d82548). See the [upstream issue](https://github.com/OpenAPITools/openapi-generator/issues/5377) for more information.

5. Add tests for the default `Configuration` behavior (ref: https://github.com/kubernetes-client/python/pull/1303 and https://github.com/kubernetes-client/python/pull/1285). The commit [1ffa61d0650e4c93e0d7f0becd2c54797eafd407](https://github.com/kubernetes-client/python/pull/1285/commits/1ffa61d0650e4c93e0d7f0becd2c54797eafd407) should be cherry-picked.

### 4. CHANGELOG

Make sure the change logs are up to date [here](https://github.com/kubernetes-client/python/blob/master/CHANGELOG.md).
If they are not, follow commits added after the last release and update/commit
the change logs to master.

Then based on the release, follow one of next two steps.

### 5. README

Update the compatibility matrix and maintenance status in the README file.

### Submit pull request

Typically after the you've completed steps 2-6 above you can push your changes
open a pull request against `kubernetes-client:release-x.y`

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

## Make distribution packages

First make sure you are using a clean version of python. Use virtualenv and
pyenv packages. Make sure you are using python 3.9.1. I would normally do this
on a clean machine:

(install [pyenv](https://github.com/yyuu/pyenv#installation))
(install [pip](https://pip.pypa.io/en/stable/installing/))
(install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/))

```bash
git clean -xdf
pyenv install -s 3.9.1
pyenv global 3.9.1
virtualenv .release
source .release/bin/activate
python --version     # Make sure you get Python 3.9.1
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

## Create Github release

Create a github release by starting from
[this page](https://github.com/kubernetes-client/python/releases).
Click the `Draft a new release button`. Name the tag the same as CLIENT_VERSION. Change
the target branch to "release-x.y". If the release is a pre-release, check the
`This is a pre-release` option.

## Announcement

Send an announcement email to dev@kubernetes.io with the subject: [ANNOUNCE] kubernetes python-client $VERSION is released

## Cleanup

```bash
deactivate
rm -rf .release
```

ref: https://packaging.python.org/distributing/
