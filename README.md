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

 

