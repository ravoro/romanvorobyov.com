title: Python: Dunder Methods

<header id="article-header" markdown="1">   
Brief on Python's
[dunder](https://docs.python.org/3/reference/datamodel.html#special-method-names){target="_blank"}
methods.
</header>

*Dunder* methods are "special" methods
*predefined* by the Python language to allow for *operator overloading*.

They are opt-in hooks, enabling developers to write custom classes that can be operated on
using standard language features *(e.g. arithmetic operators, iteration, slicing)*.

> ... defining methods with special names [i.e. dunders] ... is Python’s approach to operator overloading,
> allowing classes to define their own behavior with respect to language operators. 
> <footer>
> <cite>
>   [Python Documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names){target="_blank"}
> </cite>
> </footer>

Never create your own dunder methods. There should be no reason to.

They are hooks into Python core *(as defined by Python core)*.

> The dunder convention is a namespace reserved for the core Python team to implement their own protocols.
> Never use the namespace for your own, library-specific things!
> This defeats the whole purpose.
> <footer>
> <cite>
>   [Python double-under, double-wonder](http://www.pixelmonkey.org/2013/04/11/python-double-under-double-wonder){target="_blank"}
> </cite>
> </footer>

It helps to understand that Python operators as we know them are actually
*syntax sugar* for underlying dunder methods.

Examples of Python operators and their ultimate translations:

Syntax Sugar | Translation          
------------ | -----------
`a + b`      | `a.__add__(b)`
`a == b`     | `a.__eq__(b)`
`a[b]`       | `a.__getitem__(b)`
`a in b`     | `a.__contains__(b)`
`len(a)`     | `a.__len__()`

To make a custom class usable by an operator, simply implement the respective dunder method.

```
class SomethingCustom:
    def __add__(self, other):
        # Do any custom logic for '+' operator.
        # For example:
        return  'I just added something'
sum = SomethingCustom() + 'hello'
sum == 'I just added something'  # True
```

#### Conclusion

Dunder methods bring a native feel to custom classes.

They hook into Python core allowing a custom class to be operated on using standard language features.

<footer id="article-footer" markdown="1">
**P.S.**

For a more detailed intro into dunder methods:

- [Enriching Your Python Classes With Dunder (Magic, Special) Methods](https://dbader.org/blog/python-dunder-methods){target="_blank"}
  by Bob Belderbos.

For more technical details on dunder methods:

- [Data Model - Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names){target="_blank"}
  section of Python documentation.
</footer>
