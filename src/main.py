underscore = {}

def each(function, collection, context=None):
    """
    Iterates over a list of elements, yielding each in turn to an iteratee function. 
    Each invocation of iteratee is called with three arguments: (element, index, collection). 

    params: function, collection, [context]
    function -> a function or lambda that takes three inputs, element of the list, index, collection
    collection: the list whose elements will will be passed on the function one by one. This can be a generator as well yielding elements one by one. 
    context: an optional dict which will be available within the function as `context`

    It does not support dictionary like collections for now, but only list like collections
    """
    if context is None:
        context = {}
    try:
        function.context = context
    except AttributeError as e:
        # built in functions like print do not support this assignment
        if 'builtin_function_or_method' in e:
            print('Warning: Ignoring context for built in functions or methods')
        else:
            print('Warning: {0}'.format(e))

    for key,value in enumerate(collection):
        function(value,key,collection)
        yield value
