## Objective

You have learned how to create a package, now we will see one of the benefits of packaging:
👉 Sharing a package with your colleagues

## How do I share my code ?

Simply create a GitHub repository for your package, and then everyone will be able to install your package using:

```bash
pip install git+https://github.com/<user.github_nickname>/mlproject
```

🤔 Still not clear ?
Remember the `packgenlite` package right ?
You were able to install it in your virtual environment by running:

```bash
pip install git+https://github.com/krokrob/packgenlite
```

Well, the parameter provided to `pip` is just the decorated URL address of the [packgenlite GitHub repo](https://github.com/krokrob/packgenlite). Follow the link and inspect its code... Very similar to the one of our package 👌

Once `packgenlite` is installed, as with any package, you are able to import its modules in any python file or through ipython or a notebook:

```bash
from packgenlite.lib import get_data

get_data()
```

You are also able to play with its scripts... We will do the same thing with our package so that it allows you to share your code with other developers.

## Share your own library

You just saw how to opensource your package.

You will now share your package with all of your colleagues.

Your colleagues will install your package and run:

```python
from yourpackage.lib import try_me
```

Create a project with the `packgenlite` command:
- Create it outside of the `data-challenges` folder (`cd ~/code/<user.github_nickname>`)
- Name it as you please (avoid using dashes `-` or dots `.` in the name of your package, since this is against [package naming conventions](https://docs.python-guide.org/writing/structure/#modules) and makes importing your package harder)
- Create a `lib.py` file in the `yourpackage` directory

Your package should be structured as follows:

``` bash
.
├── MANIFEST.in
├── Makefile
├── README.md
├── notebooks
├── raw_data
├── requirements.txt
├── scripts
│   └── yourpackage-run
├── setup.py
├── tests
│   └── __init__.py
└── yourpackage
    ├── __init__.py
    ├── data
    └── lib.py
```

Then add some content:
- Add a `try_me()` function to the `lib.py` file
- Insert some code in that function, try to be creative 🎉
👉 Make sure that everything works correcly on your machine before sharing your code... You do not want other developers to discover your bugs before you 😉

Now lets publish your code:
- Create a [new public repository](https://github.com/new) on GitHub named after the name of your package
👉 The repository needs to be public, otherwise you will not be able to share your package easily with anyone...
- Follow the instructions in the `... or push an existing repository from the command line` section:

```bash
git remote add origin git@github.com:<user.github_nickname>/PACKAGE_NAME
git push -u origin master
```

🚨 Depending on the way `git` and `GitHub` are configured, the default branch of your repository may be called `master` or `main`:

The command line invite in your terminal will look either like:
``` bash
➜  yourpackage git:(master)
```

or like:
``` bash
➜  yourpackage git:(main)
```

👉 If your default branch is called main, use the command `git push -u origin main` instead 👌

Publish the `pip install` command on the slack channel of the batch, for your colleagues to install your package and run your function 🥳

💡 __the command should look like `pip install git+https://github.com/<user.github_nickname>/PACKAGE_NAME`__

Your colleagues must have done the same thing... Add all their packages to a `requirements.txt` file and test their functions 🔥

## Bonus: Pypi, the last layer to Open Source

You can skip the following section as it is a pure bonus, but definitely worth reading.

This section is for your general knowledge and will not be useful until you really want to opensource a package.

You probably wondered how to install your package with the `pip install PACKAGE_NAME` command rather than `pip install git+https://github.com/<user.github_nickname>/PACKAGE_NAME`...

### Process to fully opensource your package:

- Create two accounts, one on [PyPI](https://pypi.org/account/register/) and one on [TestPyPI](https://test.pypi.org/account/register/)
💡 __PyPI allows to officially opensource your package. TestPyPI allows to test your package before pushing to PyPI__
- Follow [this tutorial](https://anweshadas.in/how-to-upload-a-package-in-pypi-using-twine/) in order to upload your package to PyPI using [twine](https://twine.readthedocs.io/en/latest/)
