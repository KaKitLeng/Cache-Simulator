**Author**: Ka Kit Leng\
**Email**: kakit.leng@wmich.edu\
**Assignment**: Cache Simulator\
**Language**: Python3


# Introduction
The purpose of this assignment is to better understand the operation of cache memory.

# Reference Trace Files
The traces subdirectory of the handout directory contains a collection of reference trace files that you can use to evaluate the correctness of the cache simulator you write. The trace files are generated by a Linux program called valgrind. For example, typing

``` bash
linux> valgrind --log-fd=1 --tool=lackey -v --trace-mem=yes ls -l
```
On the command line runs the executable program ls -l, captures a trace of each of its memory accesses
in the order they occur, and prints them on stdout. Valgrind memory traces have the following form:

``` bash
I 0400d7d4,8
 M 0421c7f0,4
 L 04f6b868,8
 S 7ff0005c8,8
 ```
Each line denotes one or two memory accesses. The format of each line is

``` bash
[space]operation address,size
```

The operation field denotes the type of memory access: 
- “I” denotes an in- struction load
- “L” a data load
- “S” a data store
- “M” a data modify (i.e., a data load followed by a data store)

There is never a space before each “I”. There is always a space before each “M”, “L”, and “S”. The address field
specifies a 64-b hexadecimal memory address. The size field specifies the number of bytes accessed by
the operation.


# Run Instructions
Prerequisite: [Python3](https://www.python.org/downloads/)
- Enter the number of set index (s)
- Enter your preferred Associativity (E)
- Enter the number of blocks (b)
- Enter a Trace file (t)

# Example Output

``` bash
-s Number of set index bits: 4
-E Associativity (number of lines per set): 1 
-b Number of block bits: 4
-t Trace file: traces\yi.trace

hits: 4  misses: 5  evictions: 3
```

If verbose is implemented:

``` bash
-s Number of set index bits: 4
-E Associativity (number of lines per set): 1 
-b Number of block bits: 4
-t Trace file: traces\yi.trace

L 10,1 miss
M 20,1 miss hit
L 22,1 hit
S 18,1 hit
L 110,1 miss eviction
L 210,1 miss eviction
M 12,1 miss eviction hit

hits:4  misses:5  evictions:3
```

# TODO

- [ ] Implement verbose mode