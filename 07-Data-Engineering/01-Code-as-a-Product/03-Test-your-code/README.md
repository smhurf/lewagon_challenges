
## Objective

Understand how tests work and implement your first test.

Install the [code coverage](https://en.wikipedia.org/wiki/Code_coverage) package with `pip install coverage`.

💡 __The `coverage` package will be used by the `make` command when we `make test` in order to assess the amount of code covered by the tests. How does that work ? The `coverage` command installed by the package will verify whenever we run the tests how much of the code of the package gets executed. This gives us an indication of the risk of our program being buggy (0%: not great, 100% coverage: highly tested)__

## Run tests

Create two new files:

```bash
touch mlproject/lib.py
touch tests/lib_test.py
```

and copy paste the below code into them:

```python
# mlproject/lib.py

def hello_world():
    return "Hello world from mlproject"
```

```python
# tests/lib_test.py
from mlproject.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0
```


Inspect `Makefile`, and run:

```bash
make test
```

You just ran all the tests under `test/`

## Create your own test

You will now test the `haversine()` function:

- Create a `distance_test.py` file under `tests/` testing your `haversine()` function.
  *But what should I test? 🤔*
  You want to make sure the functionality of your function is correct. You can check if the distance between given coordinates is valid or if the type returned by it is the right one. It's up to you!

Run `make test` again and check that your test passes.
