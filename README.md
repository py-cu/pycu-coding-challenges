## About 

Quick programming challenges and tests

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
The files we're interested in are the `kata*.py` files and associated `kata*_tests.py` files, e.g. `kata1.py` and `kata1_tests.py`.

`kata1.py` contains some skeleton code to flesh out, e.g. 

``` python
def foo(the_input):
  """ This function should do foo and return bar """
  # put your code here
```

After you finish writing and save the file, run the tests in the associated tests file, e.g. 

``` bash
$ python kata1_tests.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
```
