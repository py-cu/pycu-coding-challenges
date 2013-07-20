## About 
Quick programming challenges and tests for Py-CU. We're still exploring, but
the idea is something close in spirit (but not implementation) to a coding dojo
-- a fun, effective, challenging way to solve interesting problems and learn a
bunch of stuff with other people.

## Setting up
(this is draft-ish)

Clone this repository (or download the .zip)

``` bash
$ git@github.com:gnarlinsky/pycu-coding-challenges.git
```

Create a virtualenv and install the required packages. 
(This is currently optional because at this point there aren't any dependencies to worry about, but hopefully later there will be.)

``` bash
$ cd pycu-coding-challenges/
$ virtualenv ve --no-site-packages  # or in another directory
$ source ve/bin/activate      # activate the virtual environment
$ pip install -r requirements.txt
```

## How to play
The files we're interested in are the `challenge*.py` files and associated
`challenge*_tests.py` files, e.g. `challenge5.py` and `challenge5_tests.py`.

`challenge5.py` contains some skeleton code to flesh out and instructions, e.g. 

``` python
def foo(the_input):
  """ This function should do foo and return bar """
  # put your code here
```

After you finish writing and save the file, run the tests in the associated tests file, e.g. 

``` bash
$ python challenge5_tests.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
```
