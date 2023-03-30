# Iterators and Iterable

* **An Iterator** is a class that has the methods `__iter__()` and `__next__()`.

* **An iterable** is any object from which the `iter` built-in function can obtain an iterator.
    * Objects implementing an `__iter__` method returning an iterator are iterable.
    * Iterables have an `__iter__` method that instantiates a new iterator every
time
    * Sequences are always iterable, as are objects implementing a __getitem__ method that
    accepts 0-based indexes.

Python obtains iterators from iterables.

```python
# tuple is an Iterable
mytuple = ("apple", "banana", "cherry")

# iter() returns an Iterator
it = iter(mytuple)                    
print(next(it))
print(next(it))
print(next(it))

# string is an Iterable
s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it  # the iterator object is discarded
        break   # exit the loop
```

## A Pythonic implementation of the Iterable via Generator function

```python
class Sentence:
    def __init__(self, text):
        self.words = text.split()

    def __repr__(self):
        return 'Sentence(%s)' % self.words

    def __iter__(self):
        for word in self.words:
            yield word
```


# Generator

Any Python function that has the `yield` keyword in its body is a generator function.
When the generator function returns, the generator object raises StopIteration.

```python
def fibonacci():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr
```
