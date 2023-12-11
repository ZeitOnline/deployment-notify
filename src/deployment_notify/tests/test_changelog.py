from ..changelog import extract_postdeploy


def test_extract_postdeploy():
    postdeploy = extract_postdeploy("""\
Changelog
=========

something else

POSTDEPLOY
- one
- two

.. towncrier release notes start

1.0.0 (2023-01-01)
------------------

- Initial release""")
    assert postdeploy == """\
- one
- two"""


def test_postdeploy_only_nothing_returns_empty():
    postdeploy = extract_postdeploy("""\
POSTDEPLOY
- nothing

.. towncrier release notes start""")
    assert postdeploy is None
