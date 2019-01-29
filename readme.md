1. To create a package use setuptools
2. Control what gets brought into namespace when using:

    from x import * 

   by overriding the \__all\__ keyworld in the \__init\__.py
3. Usage from command line locally would be to use pip install <path to package - including directory>

    For example:
    pip install /Users/jason/PycharmProjects/package_creation
4. Use as expected from a new script.
   