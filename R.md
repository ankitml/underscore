# src

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
