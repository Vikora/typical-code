# Concurrency and Parallelism in Python

**Concurrency**
is about *dealing with* lots of things at once.
* Two or more tasks are running in overlapping periods on a single processor and core.

**Parallelism**
is about *doing* lots of things at once.
* Multiple tasks or distributed parts of a task run independently and simultaneously on multiple processors.

Imagine two queues of customers. Concurrency means a single cashier serves customers by switching between two queues.
Parallelism means two cashiers simultaneously serve the two queues of customers.

**Process**
has its own address space, memory, data stack.
* P. communicate via pipes, sockets, or memory mapped files.

**Thread**
is an execution unit within a single process.
*  Threads within a process share the same memory space.


## Future

`concurrent.futures.Future` and `asyncio.Future`

An instance of either Future class represents **a deferred computation** that may or may
not have completed. This is somewhat similar to the Deferred class in Twisted, the
Future class in Tornado, and Promise in modern JavaScript.

* Futures encapsulate pending operations.

* Futures are meant to be **instantiated exclusively by the concurrency framework**.
  * A Future represents something that
will eventually run, therefore it must be scheduled to run, and that's the job of the
framework.

* Application code is not supposed to change the state of a future.


## multithreading
 
### threading.Event
This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.

An event object manages an internal flag that can be set to true with the `set()` method and reset to false with the `clear()` method. The `wait()` method blocks until the flag is true.

```python
class Foo:
    def __init__(self):
        self._first_printed = threading.Event()
        self._second_printed = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self._first_printed.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self._first_printed.wait()
        printSecond()
        self._second_printed.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self._second_printed.wait()
        printThird()
```


