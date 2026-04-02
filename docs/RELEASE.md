# Deltakit-Stim Release Procedure

Stable releases are supported with the `v*` semantic version tags.

## Stable Releases

Stable releases are performed as-needed whenever new features or critical bug fixes are made. The target audience of stable releases are typical users.

Semantic versioning communicates whether releases include any backward compatible changes so that users can decide when/whether to upgrade.

A stable release currently consists of:
- A version [tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) (human-readable label) associated with a commit.
- Assets published to PyPI (which gets added to the "Release history" there).
- Assets published to "Releases" on our GitHub repo.

"Assets" currently refers to [wheel](https://peps.python.org/pep-0427/)s (pre-built Python package format)
and sdists ("source distribution") of `deltakit-stim`.

To perform a release, the release manager needs to go through the following steps:
1. Make a PR (to `main`) where version is bumped and any other necessary changes made.
2. After PR has been merged, manually create a release using GitHub's web application. The following should be enabled in the release:
    * Tag creation (format `v<package_version>`)
    * Release notes generation
3. Publishing this release will create a source code release on GitHub and trigger the [`publish.yml workflow`](../.github/workflows/publish.yml) which publishes the wheels and sdists on Python Package Index (PyPI).

The latest stable version of `deltakit-stim` can be installed with `pip install deltakit-stim`.
