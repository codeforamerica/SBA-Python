Python Wrapper for SBA APIs (www.sba.gov/api/), currently follows PHP version 
https://github.com/codeforamerica/SBA-PHP-Library in being a thin wrapper.

For examples, see documentation for each method in api.py.

21 Jun 2011: All methods finished. Todo: Rewrite to be more 
pythonic/follow the syntax of other python wrappers more closely. Also, write 
class documentation, split each API class into its own file (similar to 
https://github.com/codeforamerica/sba_ruby).

Third Party Libraries
---------------------

Current third-party libraries we're using include:

* `mock` -- Create test stubs and mocks.
<pre><code>
    >>> from mock import Mock
    >>> from api import api
    >>> api.urlopen = Mock()
</code></pre>

* `coverage` -- Check test code coverage.
<pre><code>
    $ coverage run test.py
    .................
    -----------------
    Ran 17 tests in 0.010s

    $ coverage report -m
    Name                          Stmts   Miss  Cover   Missing
    -----------------------------------------------------------
    test                            113      0   100%   
    api/__init__                      2      0   100%   
    api/api                          42      0   100%   
    api/api_key                       2      0   100%   
    -----------------------------------------------------------
    TOTAL                           159      0   100%   
</code></pre>

* `pep8` -- Check Python files are following the PEP 8 Style Guide.
<pre><code>
    $ pep8 test.py
    test.py:12:1: E302 expected 2 blank lines, found 1
</code></pre>

