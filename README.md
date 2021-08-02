# hello-python  
```shell
# full name
python setup.py --fullname

# build help message
python -m build --help

# commands help message
python setup.py --help-commands
# create a source distribution
python setup.py sdist --formats=zip
# all source distribution formats
python setup.py sdist --help-formats

# create a built (binary) distribution
python setup.py bdist --formats=egg
# all built (binary) distribution formats
python setup.py bdist --help-formats

# create a wheel distribution
python setup.py bdist_wheel

# create an "egg" distribution
python setup.py bdist_egg

```
