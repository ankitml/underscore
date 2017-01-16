## underscore

Underscorejs port for python


## Highlights
* Supports python 3. 
* All methods are lazy and return generators (well almost all)

## Why
Underscore library has been very beneficial for working with collections in javascript. It has more than 60 functions, for manipulating, filtering, sorting, merging, grouping etc arrays in js. There is already a python port available in github called underscore.py, however it does not use generators and hence much more resource hogging. The goal of this repository is to provide very lightweight implementation in python and focus on performance along with ease of use. 

"Underscore.js is the single most depended on module on npm." Python needs its own version of expressive list manipulation library.

## Installation

This package is not yet available on pypy but you can install bleeding edge version by doing

```
pip install git+https://github.com/ankitml/underscore.git
```


## API


#### each

Iterates over an iterable, yielding each element in turn to an iteratee function. 


params: array, function/lambda
array: the list whose elements will will be passed on the function one by one. This can be a generator as well yielding elements one by one. 
function -> a function or lambda that takes either one or two inputs, element of the list, index of element. If it takes only one input then index will not be sent. 

Returns a generator of the input iterable, can be used for chaining purposes.

Example: 
```python
>>> array = [1,10,100]
>>> iteratee1 = lambda val : print(val)
>>> iteratee2 = lambda val, index: print(index)
>>> lazy_each_object = _.each(_.each(array, iteratee1), iteratee2)
This lazy object is a generator and is not executed yet. This can be done wither by casting generator into a list, which returns the original array or iterating over it.
>>> list(lazy_each_object)
>>> 1
>>> 0
>>> 10
>>> 1
>>> 100
>>> 2
Note the order or execution. All the iteratees are finished first for an element before the next element takes over. This can be changed by casting into list before passing it to next _.each method.
>>> not_so_lazy_each_object = list(_.each(list(_.each(array, iteratee1)), iteratee2))
>>> 1
>>> 10
>>> 100
>>> 0
>>> 1
>>> 2
```


#### map

Produces a new stream of values (generator) by mapping each value in array 

(list, set, tuple, generator) through a transformation function (iteratee). 
The iteratee is passed two arguments: the value, then the index (or key) of the iteration. If the iteratee can accept only one argument then only one will be sent

params: array, iteratee
    array -> a list, tuple, iterator, generator, dictionary
    iteratee -> a function or a lambda

Examples:
```python
list(_.map([1,2,3], lambda x: x*3))
[3,6,9]
list(_.map({one: 1, two: 2, three: 3}, lambda key, val: val*3))
[3,6,9]
list(_.map([[1, 2], [3, 4]], _.first))
[1,3]
```


#### reduce

Also known as inject, foldl or fold-left, reduce boils down a list of values 

into a single value. init is the initial state of the reduction, and each 
successive step of it should be returned by iteratee. The iteratee is passed 
three arguments: the current_reduced_state, then the value and index (or key) of the iteration.

If no init is passed to the initial invocation of reduce, the iteratee is not invoked on the first element of the list. The first element is instead passed as the memo in the invocation of the iteratee on the next element in the list. 

params: iterable, iteratee, init
    iterable -> a list, tuple, iterator, generator, dictionary
    iteratee -> a function or a lambda
    init -> Inital value of the reduced state

Examples:
```python
>>> total = _.reduce([1, 2, 3], lambda memo, val: memo + val, 0);
# >>> twisted_total = _.reduce([1, 2, 3], lambda memo, val, index: memo + num*index, 0);
```


#### reduce_right

Not implemented. Reduce right is also known as fold right. THere is no way this can be implemented with generators and hence skipped.



#### find

Looks through each value in the list, returning the first one that passes a truth test 

The function yields as soon as it finds an acceptable element, and doesn't traverse the entire iterable

params: iterable, conditional
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

Examples:

```python
list(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
[2]
```

Since this returns a generator with a single value "next" can also be used to extract that value
```python
next(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
2
```

TODO: What happens if nothing is matched, generator would raise an exception on next


#### select

 Looks through each value in the list, returning an array of all the values that pass a truth test (conditional). 


params: conditional, iterable
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

Examples:

```python
list(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
[2, 4, 6]
```


#### where

 Looks through each value in the list, returning an array of all the values that contain all of the key-value pairs listed in properties. 


 params: iterable, properties
     iterable-> a list/generator of dictionaries
     properties-> key value pairs which need to be in a dictionary.

 Examples:
```python
list(_.where(list_of_plays, {author: "Shakespeare", year: 1611}))
[{title: "Cymbeline", author: "Shakespeare", year: 1611}, {title: "The Tempest", author: "Shakespeare", year: 1611}]
```


#### find_where

 Looks through the list and returns the first value that matches all of the key-value pairs listed in properties. 

TODO what happens in case of no match?

params: iterable, properties
     iterable-> a list/generator of dictionaries
     properties-> key value pairs which need to be in a dictionary.

Examples:
```python
>>> list(_.findWhere(public_service_pulitzers, {"newsroom": "The New York Times"}))
>>> [{"year": 1918, "newsroom": "The New York Times",
      "reason": "For its public service in publishing in full so many official reports, documents and speeches by European statesmen relating to the progress and conduct of the war."}]
```

Alternatively, next function can be used to get the only value in the generator returned
```python
next(_.findWhere(public_service_pulitzers, {"newsroom": "The New York Times"}))
{"year": 1918, 
 "newsroom": "The New York Times",
 "reason": "For its public service in publishing in full so many official reports, documents and speeches by European statesmen relating to the progress and conduct of the war."}
```


#### reject

 Returns the values in list without the elements that the truth test (predicate) passes. The opposite of filter. 


 params: iterable, conditional
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

Examples:
```python
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
list(odds)
[1,3,5]
```


#### every

 Returns true if all of the values in the list pass the predicate truth test. Short-circuits and stops traversing the list if a false element is found. 


 params: iterable, conditional
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)
Examples:
```python
_.every([2, 4, 5], lambda x: x % 2 == 0)
False
```


#### some

 Returns true if any of the values in the list pass the predicate truth test. Short-circuits and stops traversing the list if a false element is found. 


 params: iterable, conditional
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)
Examples:
```python
_.some([2, 4, 5], lambda x: x % 2 == 0)
True
```


#### contains

Returns true if the value is present in the iterable. Use from_index to start your search at a given index.


Params: iterable, value
    iterable -> list, sequenece, set, dictionary, generator etc
    value -> Any element that is to be searched in the iterable

IMP: This method is not lazy

Examples:
```python
_.contains([1, 2, 3], 3);
True
```


#### invoke

 Calls the callable named by iteratee_name on each value in the iterable. Any extra arguments passed to invoke will be forwarded on to the method invocation. 


 Difference with _.each, _.map: each takes in the callable object instead of callable objects' name as string. Also _.invoke returns the new iterable from values returned by the callable. In this sense this is much closer to _.map.

 params: iterable, iteratee_name, arguments [optional]
    iterable -> list, sequenece, set, dictionary, generator etc
    iteratee_name -> name of the function which is available in the score while executing the code
    arguments -> optional arguments that will be passed on to the iteratee function

Examples
```python
list(_.invoke([[5, 1, 7], [3, 2, 1]], 'sorted'))
[[1, 5, 7], [1, 2, 3]]
list(_.invoke([[5, 1, 7], [3, 2, 1]], 'sorted', keyword_args={"reverse":False, "key": lambda x: x if x %2 == 0 else 0}))
 [[1, 5, 7] [3, 1, 2]]
```


#### pluck

 A convenient version of what is perhaps the most common use-case for map: extracting a list of property values from a dictionary like iterable. 

 TODO: Identify non dictionary like iterables and raise Exception

 params: iterable, property_name
    iterable-> an iterable of dictionary like objects
    property_name-> name of property which you want to extract from the dictionaries

Examples:
```python
stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
list(_.pluck(stooges, 'name'))
["moe", "larry", "curly"]
```


#### max

 Returns the maximum value in list. If a key is provided, it will 

 be used on each value to generate the criterion by which the value is ranked. If a key_func is provided it will be used as callable for every element to rank the items.
 Only one of the key options will be accepted, if both are given key_func will be ignored

 params: iterable, key [optional], key_func [optional]
    iterable-> an iterable of dictionary like objects
    key-> dictionary key for customizing comparisions in the elements of the iterable
    key_func-> a function or lambda, as custom key function that customizes comparison way

Examples:
```python
stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
next(_.max(stooges, key='age'))
{"name":'curly', "age": 60}
next(_.max(stooges, key_func=lambda x: x.get('age')))
{"name":'curly', "age": 60}
```


#### min

 Returns the minimum value in list. If a key is provided, it will 

 be used on each value to generate the criterion by which the value is ranked. If a key_func is provided it will be used as callable for every element to rank the items.
 Only one of the key options will be accepted, if both are given key_func will be ignored

 params: iterable, key [optional], key_func [optional]
    iterable-> an iterable of dictionary like objects
    key-> dictionary key for customizing comparisions in the elements of the iterable
    key_func-> a function or lambda, as custom key function that customizes comparison way

Examples:
```python
stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
next(_.max(stooges, key='age'))
{'moe': 40}
next(_.max(stooges, key_func=lambda x: x.get('age')))
{'moe': 40}
```


#### sort_by

 Returns the sorted iterable in ascending order. If a key is provided, it will 

 be used on each value to generate the criterion by which the value is ranked. If a key_func is provided it will be used as callable for every element to rank the items.
 Only one of the key options will be accepted, if both are given key_func will be ignored
 If reverse is provided, ranking is done in descending order

 params: iterable, key [optional], key_func [optional], reverse [optional]
    iterable-> an iterable of dictionary like objects
    key-> dictionary key for customizing comparisions in the elements of the iterable
    key_func-> a function or lambda, as custom key function that customizes comparison way
    reverse -> boolean, default is Ascending order, True makes is descending

Examples:
```python
stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
_.sort_by(stooges, key='age')
[{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}]
_.sort_by(stooges, key='age', reverse=True)
[{"name": 'curly', "age": 60}, {"name": 'larry', "age": 50}, {"name": 'moe', "age": 40}]
```


#### group_by

 Splits an iterable into sets, grouped by the result of running each value through iteratee. 

 If iteratee is a string instead of a function, groups by the property named by iteratee on each of the values. 

 params: iterable, iteratee
    iterable -> a list, tuple, iterator, generator
    iteratee -> a function or a lambda, taking single value as input and returning a transformed value on which iterable will be grouped

Returns a dictionary

Examples:
```python
_.group_by([1.3, 2.1, 2.4], lambda x:math.floor(x))
{1: [1.3], 2: [2.1, 2.4]}
```


#### index_by

Converts a list or iterable into a dictionary by using either key or key_func. 


params: array, key [optional], key_func [optional]
    array-> list like iterable
    key -> assuming array as array of dictionaries, key is a dictionary_key which is present in all of the dictionaries.
    key_func->  a function or lambda that takes an element of the iterable and returns the key or index for the dictionary output

Examples:
```python
stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
_.index_by(stooges, key='age');
{
    "40": {"name": 'moe', "age": 40},
    "50": {"name": 'larry', "age": 50},
    "60": {"name": 'curly', "age": 60}
}
```


#### count_by

Think of it like a harry potter sorting hat, tells you final number of students in every group.

Similar to group_by, instead of returning a list with every grouped_key, returns count of grouped elements only.

params: array, iteratee
    iterable-> list, set, generator 
    iteratee-> a function or a lambda for grouping the elements

Examples
```python
_.count_by([1, 2, 3, 4, 5], lambda x: 'even' if x % 2 == 0 else 'odd')
{"odd": 3, "even": 2}
```


#### shuffle

Returns a shuffled copy of the list.

Caution: DOes not work with unordered collections and generators

params: iterable
    iterable -> list, sequenece, 


Examples:
```python
_.shuffle([1, 2, 3, 4, 5, 6]);
[4, 1, 6, 3, 5, 2]
```


#### sample

 Produce a random sample from the list. Pass a number to return n random elements from the list. Otherwise a single random item will be returned. 


CAUTION: Does not yet work with generators
params: iterable, n_sample
    iterable -> list, sequenece, set, dictionary
    n_sample -> number of random samples to be taken from iterable

TODO: implement walker's method. current one is too inefficient
http://code.activestate.com/recipes/576564-walkers-alias-method-for-random-objects-with-diffe/
Examples:
```python
_.sample([1, 2, 3, 4, 5, 6])
[4]
_.sample([1, 2, 3, 4, 5, 6], 3)
[1, 6, 2]
```


#### size

Returns the length of an iterable. 

Caution: If this iterable is generator, this method would eat up the generator

params: iterable
    iterable -> list, sequenece, set, dictionary, generator etc

Examples:
```python
gen = (i for i in range(0,10))
_.size(gen)
10
```


#### partition

 Splits the iterable into two iterators: one whose elements all satisfy conditional and one whose elements all do not satisfy conditional.


 params: iterators, conditional
    iterable -> list, sequenece, set, dictionary, generator etc
    conditional -> a lambda or function that takes one input and returns a boolean

Examples:
```python
even, odd = _.partition([1,2,3,4,5,6,7,8,9], lambda x: x % 2 ==0)
list(even)
[2,4,6,8]
list(odd)
[1,3,5,7,9]
```


