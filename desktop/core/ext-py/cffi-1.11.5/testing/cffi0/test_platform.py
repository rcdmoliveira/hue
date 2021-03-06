import os
from cffi.ffiplatform import maybe_relative_path, flatten


def test_not_absolute():
    assert maybe_relative_path('foo/bar') == 'foo/bar'
    assert maybe_relative_path('test_platform.py') == 'test_platform.py'

def test_different_absolute():
    p = os.path.join('..', 'baz.py')
    assert maybe_relative_path(p) == p

def test_absolute_mapping():
    p = os.path.abspath('baz.py')
    assert maybe_relative_path(p) == 'baz.py'
    foobaz = os.path.join('foo', 'baz.py')
    assert maybe_relative_path(os.path.abspath(foobaz)) == foobaz

def test_flatten():
    assert flatten("foo") == "3sfoo"
    assert flatten(-10000000000000000000000000000) == \
           "-10000000000000000000000000000i"
    assert flatten([4, 5]) == "2l4i5i"
    assert flatten({4: 5}) == "1d4i5i"
    assert flatten({"foo": ("bar", "baaz")}) == "1d3sfoo2l3sbar4sbaaz"
