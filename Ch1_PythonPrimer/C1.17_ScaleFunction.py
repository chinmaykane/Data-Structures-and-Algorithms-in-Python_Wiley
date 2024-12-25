"""
Python’s parameter passing model has additional implications when a parameter is
a mutable object. Because the formal parameter is an alias for the actual parameter,
the body of the function may interact with the object in ways that change its state.
Considering again our sample invocation of the count function, if the body of the
function executes the command data.append( F ), the new entry is added to the
end of the list identified as data within the function, which is one and the same as
the list known to the caller as grades. As an aside, we note that reassigning a new
value to a formal parameter with a function body, such as by setting data = [ ],
does not alter the actual parameter; such a reassignment simply breaks the alias.
Our hypothetical example of a count method that appends a new element to a
list lacks common sense. There is no reason to expect such a behavior, and it would
be quite a poor design to have such an unexpected effect on the parameter. There
are, however, many legitimate cases in which a function may be designed (and
clearly documented) to modify the state of a parameter. As a concrete example,
we present the following implementation of a method named scale that’s primary
purpose is to multiply all entries of a numeric data set by a given factor.

def scale(data, factor):
    for j in range(len(data)):
    data[j] = factor

Had we implemented the scale function (page 25) as follows, does it work
properly?

def scale(data, factor):
    for val in data:
    val *= factor

Explain why or why not."""