#! python3
"""@package docstring

Documentation for this module.

More details.
"""

class Egg(object):
    """OUTLINE in one line
    
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).
    
    Args:
        name: label
        range: range
        value: std_value (default is None)
    
    Args:
        *args : ...
        **kwargs : ...
    
    Attributes:
        class attributes
    
    Note:
        The style args and the explanation aligned with colon.
    """
    def __init__(self, *args, **kwargs):
        """Initialize Egg
        
        Describe args in class doc.
        Describe what __init__ does.
        
        Note: This doc:str does not appear in a tooltip.
        """
        pass

    def func(self, x, y):
        """OUTLINE in one line.
        
        (override) If there is overridden.
                   Select mode in
                   {0:no-wrap, 1:word-wrap, 2:char-wrap, 3:whitespace-wrap, None:toggle}
        
        Args:
            x : x-value
            y : y-value
        
        Returns:
            norm (float): norm value
        
        Note:
            The style args and the explanation aligned with colon.
        """
        return 42


def dummy_function_example(name, foo=None):
    r"""
    The docstring in the function should fully explain what the function is
    for and how to use it

    * this is a bullet list
    * with multiple entries and some text in *italic* and even **bold**.
      The bullet list items can span multiple lines which are indented

    .. warning:: bullet (as well as enumerated) lists have to start and end
       with an empty line

    1. Single backquotes are for **references** to other documented items.
       For example `basf2.Module` will link to the documentation of the class
       Module in the python module basf2. A different link name and link
       target can be specified with <>: `Module class <basf2.Module>` will
       link to basf2.Module but the link will read "Module class"
    2. Double backquotes are for ``literal text``.

    .. warning:: this is different to markdown where single backquotes are
       usually used for literal text

    3. Links to external websites are usually of the form `Link Text <http://example.com>`_.

    .. note:: there is an underscore at the end of links

    4. math is supported either inline :math:`f(x) = \sum_{x=i}^N x^i` or as
       display verssion:

       .. math::

          f(x) = \sum_{i=1}^N x^i

       .. seealso:: `Math support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/math.html>`_

    5. The easiest way for code example is the "doctest" syntax: Start a new
       paragaph after an empty line with ``>>>`` followed by the python
       statements and (optionally) the expected output of these statements.

       >>> dummy_function_example("some name", foo="bar")
       "Hello some name, Lord of bar"

       .. seealso:: `Showing code examples <http://www.sphinx-doc.org/en/stable/markup/code.html>`_

    6. To document parameters and return types please use the :ref:`googlestyle` as shown below:

    Note:
      For class members please do not include the ``self`` parameter in this list

    Parameters:
      name (str): Description of the first parameter
                  Can also span multiple lines if indented properly
      foo: Second parameter but no type given

    Returns:
      Description of the return value

    See Also:
      Some references to other functions
    """
    pass


if __name__ == "__main__":
    from mwx import typename
    
    print(typename(Egg.func))
    print(typename(Egg.func, docp=1))
    print(typename(Egg.func, docp=1, qualp=1))
