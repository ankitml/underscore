## Underscorejs' python port

Highlights
* Supports python 3. 
* All methods lazy (returns generators)

### Why
Underscore library has been very beneficial for working with collections in javascript. It has more than 60 functions, for manipulating, filtering, sorting, merging, grouping etc arrays in js. There is already a python port available in github called underscore.py, however it does not use generators and hence much more resource hogging. The goal of this repository is to provide very lightweight implementation in python and focus on performance along with ease of use. 

"Underscore.js is the single most depended on module on npm." Python needs its own version of expressive list manipulation library.

### Tutorial

import pyunderscore as _

    _.each(lambda val, key, lst: print(key, val, context), [1,10,100], context='constant')

