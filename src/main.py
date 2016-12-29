import itertools
import functools
from types import GeneratorType

iteratee_needs_arguments = lambda func, n: func.__code__.co_argcount == n
function_needs_arguments = lambda func, n: func.__code__.co_argcount == n


def each(array, iteratee):
    """
    Iterates over a list, yielding each element in turn to an iteratee function. 
    Each invocation of iteratee is called with two arguments: (element, index). 

    params: array, function/lambda
    array: the list whose elements will will be passed on the function one by one. This can be a generator as well yielding elements one by one. 
    function -> a function or lambda that takes two inputs, element of the list, index of element. If it takes only one input then index will not be sent. 

    Returns a generator of all the elements, hence can be chained.

    Example: 
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
    """
    # list, sets, tuples, generators
    if iteratee_needs_arguments(iteratee, 1):
        for key,value in enumerate(array):
            iteratee(value)
            yield value
    if iteratee_needs_arguments(iteratee, 2):
        for key,value in enumerate(array):
            iteratee(value,key)
            yield value


def map(array, iteratee):
    """
    Produces a new stream of values (generator) by mapping each value in array 
    (list, set, tuple, generator) through a transformation function (iteratee). 
    The iteratee is passed two arguments: the value, then the index (or key) of the iteration. If the iteratee can accept only one argument then only one will be sent

    params: array, iteratee
        array -> a list, tuple, iterator, generator, dictionary
        iteratee -> a function or a lambda

    Examples:
    >>> list(_.map([1,2,3], lambda x: x*3))
    >>> [3,6,9]
    >>> list(_.map({one: 1, two: 2, three: 3}, lambda key, val: val*3))
    >>> [3,6,9]
    >>> list(_.map([[1, 2], [3, 4]], _.first))
    >>> [1,3]
    """
    if iteratee_needs_arguments(iteratee, 1):
        for index, item in enumerate(array):
            yield iteratee(item)
    if iteratee_needs_arguments(iteratee, 2):
        for index, item in enumerate(array):
            yield iteratee(item, index)


def reduce(array, iteratee, init=None):
    """
    Also known as inject, foldl or fold-left, reduce boils down a list of values 
    into a single value. init is the initial state of the reduction, and each 
    successive step of it should be returned by iteratee. The iteratee is passed 
    three arguments: the current_reduced_state, then the value and index (or key) of the iteration.

    If no init is passed to the initial invocation of reduce, the iteratee is not invoked on the first element of the list. The first element is instead passed as the memo in the invocation of the iteratee on the next element in the list. 

    params: array, iteratee, init
        array -> a list, tuple, iterator, generator, dictionary
        iteratee -> a function or a lambda
        init -> Inital value of the reduced state

    Examples:
    >>> total = _.reduce([1, 2, 3], lambda memo, val: memo + val, 0);
    >>> twisted_total = _.reduce([1, 2, 3], lambda memo, val, index: memo + num*index, 0);
    """

    return functools.reduce(iteratee, array, init)


def reduce_right(array, iteratee, init=None):
    """
    Not implemented. Reduce right is also known as fold right. THere is no way this can be implemented with generators and hence skipped.
    """
    raise NotImplementedError("Reduce right is not compatible with generators")


def find(iterable, conditional):
    """
    Looks through each value in the list, returning the first one that passes a truth test 
    The function yields as soon as it finds an acceptable element, and doesn't traverse the entire iterable

    params: iterable, conditional
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

    Examples:

    >>> list(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
    >>> [2]
    
    Since this returns a generator with a single value "next" can also be used to extract that value
    >>> next(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
    >>> 2

    TODO: What happens if nothing is matched, generator would raise an exception on next
    """
    for element in collection:
        if conditional(element):
            yield element
            break


def filter(iterable, conditional):
    """
     Looks through each value in the list, returning an array of all the values that pass a truth test (conditional). 

    params: conditional, iterable
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

    Examples:

    >>> list(_.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
    >>> [2, 4, 6]
    
    """
    return filter(conditional, array)


def where(iterable, properties):
    """
     Looks through each value in the list, returning an array of all the values that contain all of the key-value pairs listed in properties. 

     params: iterable, properties
         iterable-> a list/generator of dictionaries
         properties-> key value pairs which need to be in a dictionary.

     Examples:
    >>> list(_.where(list_of_plays, {author: "Shakespeare", year: 1611}))

    """
    items_to_be_checked = properties.items()
    for dictionary in array:
        if not isinstance(dictionary, dict):
            raise TypeError('"array" should be a collection of dictionaries only')
        if items_to_be_checked <= dictionary.items():
            yield dictionary


def find_where(iterable, properties):
    """
     Looks through the list and returns the first value that matches all of the key-value pairs listed in properties. 
    TODO what happens in case of no match?
    
    params: iterable, properties
         iterable-> a list/generator of dictionaries
         properties-> key value pairs which need to be in a dictionary.

    Examples:
    >>> list(_.findWhere(public_service_pulitzers, {"newsroom": "The New York Times"}))
    >>> [{"year": 1918, "newsroom": "The New York Times",
          "reason": "For its public service in publishing in full so many official reports, documents and speeches by European statesmen relating to the progress and conduct of the war."}]

    Alternatively, next function can be used to get the only value in the generator returned
    >>> next(_.findWhere(public_service_pulitzers, {"newsroom": "The New York Times"}))
    >>> {"year": 1918, 
    >>>  "newsroom": "The New York Times",
    >>>  "reason": "For its public service in publishing in full so many official reports, documents and speeches by European statesmen relating to the progress and conduct of the war."}
    """
    yield next(where(iterable, properties))


def reject(iterable, conditional=None):
    """
     Returns the values in list without the elements that the truth test (predicate) passes. The opposite of filter. 

     params: iterable, conditional
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)

    Examples:
    >>> odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
    >>> list(odds)
    >>> [1,3,5]
    """
    return reject = itertools.filterfalse(conditional, iterable)


def every(iterable, conditional=None):
    """
     Returns true if all of the values in the list pass the predicate truth test. Short-circuits and stops traversing the list if a false element is found. 

     params: iterable, conditional
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)
    Examples:
    >>> _.every([2, 4, 5], lambda x: x % 2 == 0)
    >>> False
    """
    if conditional is None:
        return all(iterable)
    if function_needs_arguments(conditional, 1):
        pass
    if function_needs_arguments(conditional, 2):
        pass


def some(iterable, conditional=None):
    """
     Returns true if any of the values in the list pass the predicate truth test. Short-circuits and stops traversing the list if a false element is found. 

     params: iterable, conditional
        iterable -> list, sequenece, set, dictionary, generator etc
        conditional -> a lambda or function that takes one or two inputs, first is element from iterable, second is index (optional)
    Examples:
    >>> _.some([2, 4, 5], lambda x: x % 2 == 0)
    >>> True
    """
    if conditional is None:
        return all(iterable)
    if function_needs_arguments(conditional, 1):
        pass
    if function_needs_arguments(conditional, 2):
        pass


def contains(iterable, value, from_index=None):
    """
    Returns true if the value is present in the iterable. Use from_index to start your search at a given index.

    Params: iterable, value
        iterable -> list, sequenece, set, dictionary, generator etc
        value -> Any element that is to be searched in the iterable

    IMP: This method is not lazy

    Examples:
    >>> _.contains([1, 2, 3], 3);
    >>> True
    """
    pass


def invoke(iterable, iteratee_name, arguments=None, keyword_args=None):
    """
     Calls the callable named by iteratee_name on each value in the iterable. Any extra arguments passed to invoke will be forwarded on to the method invocation. 

     Difference with _.each, _.map: each takes in the callable object instead of callable objects' name as string. Also _.invoke returns the new iterable from values returned by the callable. In this sense this is much closer to _.map.

     params: iterable, iteratee_name, arguments [optional]
        iterable -> list, sequenece, set, dictionary, generator etc
        iteratee_name -> name of the function which is available in the score while executing the code
        arguments -> optional arguments that will be passed on to the iteratee function

    Examples
    >>> list(_.invoke([[5, 1, 7], [3, 2, 1]], 'sorted'))
    >>> [[1, 5, 7], [1, 2, 3]]
    >>> list(_.invoke([[5, 1, 7], [3, 2, 1]], 'sorted', keyword_args={"reverse":False, "key": lambda x: x if x %2 == 0 else 0}))
    >>>  [[1, 5, 7] [3, 1, 2]]
    """
    pass


def pluck(iterable, property_name):
    """
     A convenient version of what is perhaps the most common use-case for map: extracting a list of property values from a dictionary like iterable. 
     TODO: Identify non dictionary like iterables and raise Exception

     params: iterable, property_name
        iterable-> an iterable of dictionary like objects
        property_name-> name of property which you want to extract from the dictionaries

    Examples:
    >>> stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
    >>> list(_.pluck(stooges, 'name'))
    >>> ["moe", "larry", "curly"]
    """
    pass


def max(iterable, key=None, key_func=None):
    """
     Returns the maximum value in list. If a key is provided, it will 
     be used on each value to generate the criterion by which the value is ranked. If a key_func is provided it will be used as callable for every element to rank the items.
     Only one of the key options will be accepted, if both are given key_func will be ignored
    
     params: iterable, key [optional], key_func [optional]
        iterable-> an iterable of dictionary like objects
        key-> dictionary key for customizing comparisions in the elements of the iterable
        key_func-> a function or lambda, as custom key function that customizes comparison way

    Examples:
    >>> stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
    >>> next(_.max(stooges, key='age'))
    >>> {'curly': 60}
    >>> next(_.max(stooges, key_func=lambda x: x.get('age')))
    >>> {'curly': 60}

    """
    pass


def min(iterable, key=None, key_func=None):
    """
     Returns the minimum value in list. If a key is provided, it will 
     be used on each value to generate the criterion by which the value is ranked. If a key_func is provided it will be used as callable for every element to rank the items.
     Only one of the key options will be accepted, if both are given key_func will be ignored
    
     params: iterable, key [optional], key_func [optional]
        iterable-> an iterable of dictionary like objects
        key-> dictionary key for customizing comparisions in the elements of the iterable
        key_func-> a function or lambda, as custom key function that customizes comparison way

    Examples:
    >>> stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
    >>> next(_.max(stooges, key='age'))
    >>> {'moe': 40}
    >>> next(_.max(stooges, key_func=lambda x: x.get('age')))
    >>> {'moe': 40}

    """
    pass


def sort_by(iterable, key=None, key_func=None, reverse=False):
    """
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
    >>> stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
    >>> next(_.sort_by(stooges, key='age'))
    >>> [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}]
    >>> next(_.sort_by(stooges, key='age', reverse=True))
    >>> [{"name": 'curly', "age": 60}, {"name": 'larry', "age": 50}, {"name": 'moe', "age": 40}]

    """
    pass


def group_by(iterable, iteratee):
    """
     Splits an iterable into sets, grouped by the result of running each value through iteratee. 
     If iteratee is a string instead of a function, groups by the property named by iteratee on each of the values. 

     params: iterable, iteratee
        iterable -> a list, tuple, iterator, generator
        iteratee -> a function or a lambda, taking single value as input and returning a transformed value on which iterable will be grouped

    Returns a dictionary

     Examples:
     >>> _.group_by([1.3, 2.1, 2.4], lambda x:math.floor(x))
     >>> {1: [1.3], 2: [2.1, 2.4]}
    """
    return itertools.groupby(collection, function)


def index_by(array, key=None, key_func=None):
    """
    Converts a list or iterable into a dictionary by using either key or key_func. If nothing is provided, uses sequential numbers starting from 0 as indexses.

    params: array, key [optional], key_func [optional]
        array-> list like iterable
        key -> assuming array as array of dictionaries, key is a dictionary_key which is present in all of the dictionaries.
        key_func->  a function or lambda that takes an element of the iterable and returns the key or index for the dictionary output

    Examples:
    >>> stooges = [{"name": 'moe', "age": 40}, {"name": 'larry', "age": 50}, {"name": 'curly', "age": 60}];
    >>> _.indexBy(stooges, 'age');
    >>> {
    >>>     "40": {"name": 'moe', "age": 40},
    >>>     "50": {"name": 'larry', "age": 50},
    >>>     "60": {"name": 'curly', "age": 60}
    >>> }
    """
    pass



