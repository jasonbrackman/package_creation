"""

https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

My Notes:

If I need to define what gets brought into scope when using 'from package_name import *' - it can be defined in the
__all__ keyword witch expects a list() of zero to N modules.


Listing the modules contained in the package within the __all__ list() keyword allows for importing like:

in __init__.py:
    __stuff__ = ['stuff']

Called from script using the package after installation:

    from jason_package import *
    print(stuff.add(5, 6))
    >> 11

if the __init__.py file does not contain the modules within the package -- then the following happens:


    from jason_package import *
    print(stuff.add(5, 6))
    >> Traceback ...
    >> NameError: name 'stuff' is not defined

The following will work no matter what:

    import jason_package.stuff
    print(jason_package.stuff.add(5, 6))

    from jason_package import stuff
    print(stuff.add(5, 6))
    stuff.get_cwd()

"""

__all__ = []
