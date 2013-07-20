## About 

Quick programming challenges and tests... *Note -- this does not really conform to the popular idea of coding dojo practices (not explicitly pair programming; kata1 is not really a problem to solve as such... etc.). We're just exploring the concept of solve-stuff-on-projector.... We'll think of a better name later.*

## Setting up
(this is draft-ish)

Clone this repository (or download the .zip)

``` bash
$ git@github.com:gnarlinsky/pycu-coding-dojo-katas.git
```

Create a virtualenv and install the required packages. 
(This is currently optional because at this point there aren't any dependencies to worry about, but hopefully later there will be.)

``` bash
$ cd pycu-coding-dojo-katas/
$ virtualenv ve --no-site-packages  # or in another directory
$ source ve/bin/activate      # activate the virtual environment
$ pip install -r requirements.txt
```

## How to play
The files we're interested in are the `kata*.py` files and associated `kata*_tests.py` files, e.g. `kata5.py` and `kata5_tests.py`.

`kata5.py` contains some skeleton code to flesh out and instructions, e.g. 

``` python
def foo(the_input):
  """ This function should do foo and return bar """
  # put your code here
```

After you finish writing and save the file, run the tests in the associated tests file, e.g. 

``` bash
$ python kata5_tests.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
```
