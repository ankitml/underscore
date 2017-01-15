"""
Underscorejs port for python

### Highlights
* Supports python 3. 
* All methods are lazy and return generators (well almost all)

### Why
Underscore library has been very beneficial for working with collections in javascript. It has more than 60 functions, for manipulating, filtering, sorting, merging, grouping etc arrays in js. There is already a python port available in github called underscore.py, however it does not use generators and hence much more resource hogging. The goal of this repository is to provide very lightweight implementation in python and focus on performance along with ease of use. 

"Underscore.js is the single most depended on module on npm." Python needs its own version of expressive list manipulation library.
"""

from .collection import (each, map, reduce, reduce_right, find, select,
                          where, find_where, reject, every, some, contains,
                          invoke, pluck, max, min, sort_by, group_by, index_by, 
                          count_by, shuffle, sample, size, partition)

from .array import (flatten)

__all__ = [
        'each', 'map', 'reduce', 'reduce_right', 'find', 'select',
        'where', 'find_where', 'reject', 'every', 'some', 'contains',
        'invoke', 'pluck', 'max', 'min', 'sort_by', 'group_by', 
        'index_by', 'count_by', 'shuffle', 'sample', 'size', 'partition',
        'flatten'
        ]
