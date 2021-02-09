**The goal of today's recap is to go over the process of creating a new package, understand the purpose of different files inside it and practice Continuous Integration and the Continuous Deployment.**
<br><br>


## Let's start and play a quiz on Slack 🎲
It's best to open the **Slack app on your phone** so that you can see lecturer's screen on your computer at all times.

<br>

### 🤔 How can you create a new package?

1️⃣ `pip install package-name`

2️⃣ `mkdir package-name`

3️⃣ `packgenlite package-name`

<details><summary markdown='span'>View solution
</summary>

**3️⃣ `packgenlite package-name`**

In order to create a new package you can run:

`packgenlite bbquote`

`cd bbquote`

`tree`

You should see the entire project structure created by the `packgenlite` tool.
</details>
<br><br>

### 🤔 Where can you create a new method that will belong to the package?

1️⃣ I would create a new `py` file within the `bbqoute` directory containing `init.py`.

2️⃣ I would create the method in the `init.py` file.

3️⃣ I would add the new command in the `Makefile`

<details><summary markdown='span'>View solution
</summary>

**1️⃣ I would create a new `*.py` file within the `bbqoute` directory containing `init.py`.**


```bash
touch bbquote/lib.py
```

```python
# bbquote/lib.py
import requests

def get_quote():
	url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
	response = requests.get(url).json()[0]

	return f"'{response['quote']}' \n> {response['author']}"

if __name__ == "__main__":
	print(get_quote())
```

</details>
<br><br>

### 🤔 Can you call the method from anywhere on your machine at this point?

1️⃣ Yes

2️⃣ No

<details><summary markdown='span'>View solution
</summary>

**2️⃣ No**

You can't as long as the package is not **installed** on your system.
In order to be able to do that you have to run:
`pip install -e .`
which will make the package executable from any location and will also listen to **any updates of the package files** (similar to `%autoreload`)
</details>
<br><br>

### 🤔 You can now call the method by importing it from `bbquote.lib` anywhere on your machine or you can execute the `lib.py` file directly by running: `python bbquote/lib.py`. What can you do to be able to run `bbquote-run` in the Terminal at any location and achieve the same result?

1️⃣ Add the method to `requirements.txt`

2️⃣ Create a script which will import and call the method

3️⃣ Create a new directory `bbquote-run` and add the `lib.py` file containing the method inside

<details><summary markdown='span'>View solution
</summary>

**2️⃣ Create a script which will import and call the method**


Script is an executable file that you can run from the Terminal. They are are useful with automation of the engineering tasks.
In order to convert a python file into a script you have to add two additional headers to the file and then the code which should be executed upon running the script.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

Don't forget to add the script to your `setup.py` file!
</details>
<br><br>

### 🤔 Let's now write a test for our `get_quote` method. But wait, why do we even need a test?

1️⃣ We want to make sure our package and its methods are working correctly in different circumstances

2️⃣ In case our teammate is updating the code, we are making sure the updates will not crash the package functionality

3️⃣ Tests are part of Continuous Integration - it helps to maintain the quality of our code before commiting the merge on a remote repository.

4️⃣ All of the above are correct.

<details><summary markdown='span'>View solution
</summary>

**4️⃣ All of the above are correct.**

There are multiple reasons for introducing testing in our projects and all of the above are correct. The right question is: why _wouldn't_ you introduce testing? 🤔
</details>
<br><br>

### 🤔 Let's expose our project through a public url. How you we do it?

1️⃣ `git push production master`

2️⃣ The repository is public, we don't need to do anything.

3️⃣ We can create a new app on Heroku and push our code with additional configuration.

4️⃣ None of the above.

<details><summary markdown='span'>View solution
</summary>

**3️⃣ We can create a new app on Heroku and push our code with additional configuration.**

In order to be able to display our project on an accessible url we have to use a cloud platform enabling us to build, run and operate applications. Heroku is one of such providers. In order to deploy our application and display the functionality of the `get_quote` method we can:

1. Create an `app.py` file with simple frontend calling the method

2. Add a `setup.sh` and `Procfile` for configuration

3. Create a new app on heroku by running: `heroku create <unique-app-name>`

4. Push our code to Heroku: `git push heroku master`

5. Set the dynos to run our web application: `heroku ps:scale web=1`


In case the application has an error, don't forget to check the logs: `heroku logs --tail`.
</details>
<br><br>

### 🤔 Ok, this seems like a lot of pushing: `git push origin`, `git push heroku`... Can we automate it somehow?

1️⃣ Yes

2️⃣ No

<details><summary markdown='span'>View solution
</summary>

**1️⃣ Yes**

Yes, this process is called Continuous Deployment. With additional configuration in the `pythonpackage.yml` we can ask Github to deploy the latest code to Heroku for us if all the tests will pass.

</details>
