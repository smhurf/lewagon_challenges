## Objective

Create your first CI (Continuous Integration) pipeline

## Observe your first CI pipeline

Normally here you should just sit and observe.

1. Go to the GitHub Page of the repository you created in the last exercises
2. Click on `Actions` which is the GitHub name for CI-CD `actions`
3. click on your latest commit, you should see that GitHub executed your CI pipeline for you

💡 How on earth did it happen ?
 👉 `packgenlite` created for you a file under `.github/workflows/pythonpackage.yml` at the root of your package similar to this one. The tests validation step is commented by default, but you may uncomment it if you wrote some tests.

```yaml
name: Python package

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Say hello
      run: |
        echo "Hello, World!"
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Install package and test
      run: |
        make install test clean

    strategy:
      matrix:
        python-version: [3.7]
```

With this [YAML](https://en.wikipedia.org/wiki/YAML) file (see YAML as a config file just like a JSON file in python):
 👉 every time you push a modification to your `master` (or `main`) branch in your GitHub repository, the CI pipeline above will execute the following steps:
- Get a Docker image with Ubuntu installed (we will talk more about Docker in the coming days, for now you can think of it as GitHub generating a full environment in which to run the Continuous Integration steps each time you push new code)
- Say `Hello` to the World 😉
- Configure python version to 3
- Upgrade pip and install the requirements listed in your package
- Run your tests using `make install test clean`, meaning:
  => install the package
  => run the tests
  => clean temporary files once the tests are done

🚨 The Continuous Integration will stop at the first failing step

Once your have implemented tests for the functionalities of your package, having them run automatically on GitHub instead of your own machine is extremely convenient 👍

**NB: Here we setup the CI part of the CI/CD lifecycle of a software, we can easily imagine that once GitHub passed all the tests, you want to deploy your code somewhere 👉 you will see that in the next challenge**
