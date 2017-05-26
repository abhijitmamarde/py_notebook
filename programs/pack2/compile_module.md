# Distributing Compiled Python Program

## What?

To *distribute working Python program*, **without** any `.py` *source files*

## How?

Create compiled (`.pyc` files) for all python source (`.py` files).

Command -

```
$ python3 -m compileall -b .
```

This will create `.pyc` file for each `.py` file. Once this is done, you can remove (or move) all `.py` files and share folder/directory with only `.pyc`files.

This way you can run your program/app by:

```
$ python3 main.pyc
```

instead of:

```
$ python3 main.py
```

