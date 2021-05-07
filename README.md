# jsonasobj
[![Latest Version](https://img.shields.io/pypi/pyversions/jsonasobj.svg)](https://pypi.python.org/pypi/jsonasobj)
[![Pyversions](https://img.shields.io/pypi/v/jsonasobj.svg)](https://pypi.python.org/pypi/jsonasobj) 
[![License](https://pypip.in/license/jsonasobj/badge.svg)](https://pypi.python.org/pypi/jsonasobj/)
![](https://github.com/hsolbrig/jsonasobj/workflows/Build/badge.svg)

## Deprecated
There were a number of breaking, albeit highly useful changes in the 2.0.x branch.  Unfortunately, poor requirements
hygiene on my part made it virtually impossible to gracefully migrate to this new branch.  (Note to self: when using
SemVer, 'jsonasobj = ">=1.3.1"` allows version 2.0.0 in w/o complaint.  "~1.3" is equivalent to ">= 1.3, == 1.*".  See
https://www.python.org/dev/peps/pep-0440/#compatible-release for details.).

Future development will occur on https://github.com/hsolbrig/jsonasobj2.

## Revision History
* 1.1.0 -- Method signatures all have full typing, `load` function will take a file name, a url -or- an open file as an argument 
* 1.2.0 -- added non-protected access methods and changed copyright
* 1.2.1 -- fixed issue #4
* 1.3.0 -- added user filtr to as_json and _as_json_dumps functions, fixed issue #5
* 1.3.1 -- adjusted filtr so objects 

**See:** [Jupyter notebook](notebooks/readme.ipynb) for documentation
