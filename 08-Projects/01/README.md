# Start your final project :rocket:

## Setup the project

<details>
  <summary markdown='span'><strong>I am the project leader</strong></summary>
Let's create a new project:

```bash
cd ~/code/<user.github_nickname>
packgenlite project_name
cd project_name
```

Then create a GitHub repository and push your project:

```bash
gh repo create
git push origin master
```

Finally, add your teammates as collaborators on GitHub.
</details>

<details>
  <summary markdown='span'><strong>I am a teammate</strong></summary>
Let's clone the project:

```bash
mkdir ~/code/<PROJECT_LEADER_GITHUB_NICKNAME> && cd "$_"
git clone git@github.com:<PROJECT_LEADER_GITHUB_NICKNAME>/<PROJECT_NAME>.git
cd project_name
```

Then add a `raw_data` directory (as it is not tracked by `git`):

```bash
mkdir raw_data
```

You're good to go.
</details>

## Setup a new `virtualenv` (opt.)

First, we will create a virtual env for the project:

```bash
pyenv virtualenv project_name
```

Then, we need to tell pyenv that we want to use this virtual env for our project. In order to do that, let's go to the directory of the project:

<details>
  <summary markdown='span'><strong>I am the project leader</strong></summary>


```bash
cd ~/code/<user.github_nickname>/<PROJECT_NAME>
```
</details>

<details>
  <summary markdown='span'><strong>I am a teammate</strong></summary>


```bash
cd ~/code/<PROJECT_LEADER_GITHUB_NICKNAME>/<PROJECT_NAME>
```
</details>

An run:

```bash
pyenv local project_name
```

This command creates a `.python-version` file in the directory of the project containing the name of the virtual env (`cat .python-version`). This is what allows pyenv to know which virtual env to use

👉 From now on, all the commands that you run in the directory (or in any sub directory) of your project will be using the virtual env of your project

👉 All the commands that you run outside of the directory of your project will continue to use the lewagon virtual env that you used during the bootcamp

🚨 This applies in particular to jupyter notebooks: make sure that your are located inside of the directory of your project when running `jupyter notebook` if you want to run in the virtual env of your project

## Usage of your virtual env

Another way to toggle the virtual env between your new virtual env and the lewagon virtual env is to force the usage of a specific virtual env in a terminal window, independently of the directory in which the commands are executed.

In order to go that, you can either switch to the virtual env of your project for a terminal window:

```bash
pyenv activate project_name
```

Or revert back to the lewagon virtual env that you used during the bootcamp:

```bash
pyenv activate lewagon
```

👉 If you want to revert back to the previous behavior where the virtual env depends on the directory in which you are, just open a new window

### Install minimal packages

```bash
pip install --upgrade pip
pip install -r https://gist.githubusercontent.com/krokrob/53ab953bbec16c96b9938fcaebf2b199/raw/9035bbf12922840905ef1fbbabc459dc565b79a3/minimal_requirements.txt
pip list
```

## Split the work

1. Brainstorm the objectives of the project with your team
2. Write 4-8 parallel jobs
3. Each teammate take one job and split it into small task

You can use Post-it, a [Trello](https://trello.com/) board, GitHub [Projects](https://docs.github.com/en/github/managing-your-work-on-github/creating-a-project-board) or any other project management tool your want to drive your project tasks.
