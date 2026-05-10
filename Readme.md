
# Python S-Expression Object Model

There are many variants of <a href="https://en.wikipedia.org/wiki/S-expression"> S-Expression</a>. This module here only deals with the *prefix notation*, where the first element
of an expression is expected to be an operator, which is referred to as the
``<key>`` in this module. The module provides a parser `SexpParser` that
converts a python list-based expression into a python object model. Each
expression in the list-based S-Expression representation is defined as a
recursive ``list`` representation in the form of ::

    [ <line number>, <key>, <value>... ]

where there may be none or multiple ``<values>`` of either an atom (i.e. plain
string) or another list-based S-Expression. `SexpParser` assumes the ``<key>``
here is a plain string. The ``<line number>`` not being part of the
conventional S-Expression is only here for debugging purpose

function `parseSexp()` can be used to convert plain text form S-Expression into
the list-based representation

The class `Sexp` is the top class for objects representing a parsed
expression.

If you only need a non-semantic-checking parser, you can use `SexpParser` as
it is.  For the usage of the object model produced by `SexpParser`, see the
project <a href=http://github.com/realthunder/kicad_parser>here </a>


## Quick Start

In order to construct a s-expr parser object (SexpParser) use the following command:

```
import sexp_parser
import pathlib

sym_path = pathlib.Path("path/to/my/sexpr_file");

with sym_path.open("r") as f:
    sym_sexpr = sexp_parser.SexpParser(sexp_parser.parseSexp(f.read()));
```

The sexp_parser.parseSexp function will take the sexpr_file as a string input. Then it parses the string and returns a nested list respresentation of the sexpr objects. The sexp_parser.SexpParser then takes the nested list representation and converts it into a namespace of sexpr objects. To print the sexpr object as a string use the following:

```
print(sym_sexpr.__repr__());
```

To print the sexpr objects (attributes) of the sym_sexpr namespace use:

```
print(sym_sexpr);
```
To access the attribute objects simply use the following:
```
# first option
sym_sexpr['attribute_name']

#second option
sym_sexpr.attribute_name
```
Quick tip: values that are not accessable by an attribute name are denoted by a number. For example take this sexpr:

```
(pin power_in line
    (at 2.54 5.08 0)
    (length 5.08)
    (name "VCC"
      (effects
        (font
          (size 1.27 1.27))))
    (number "A5"
      (effects
        (font
          (size 1.27 1.27)
        )
      )
    )
)
```
The corresponding attribute names are: 
```
odict_keys([0, 1, 'at', 'length', 'name', 'number'])
```
Here the numbers 0 and 1 correspond to the values **power_in** and **line**.