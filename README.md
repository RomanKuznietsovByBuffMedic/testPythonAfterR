# How use Git and GitHub?

Just make step-by-step from 
[this](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/)
tutorial.

To understand what is happening and why, it is better to read 
[this](https://git-scm.com/book/en/v2).

>Tip: from the beginning, quickly review the section, if it is complicated or you do not know how to use it right now --- skip it.

## Repository name
The name of the repository from GitHub will be the name of the folder with the project on the local machine.

*Example*: 

```
`[GITHUB NAME] / MyRepository` => `[PATH TO FOLDER]/MyRepository` 
```

## Before use
In the terminal, always check the folder you are in. 

*Example*: 

don't do this
```
user@machine: [SOME PATH]/VSCODE/$ git add .
```
do this
```
user@machine: [SOME PATH]/VSCODE/MyRepository$ git add .
```
for added files from "MyRepository"


## Repository path
In the terminal before `git clone [HTTPS ADDRESS]` go to the folder where the folder from GitHub will be created.

*Example*: 

```
$ cd [PATH TO FOLDER]
$ git clone [HTTPS ADDRESS]
```

This make project folder `[PATH TO FOLDER]/MyRepository`.

## First push
The first time you use `git push` use the branch that is shown in `git status`.

*Example*: 

```
$ git status
On branch main

some text

$ git push origin main
```

## How everyday use?

### If you don't create files
```
git commit -am "[MESSAGE]"
git push
```
### Else
```
git add .
git commit -m "[MESSAGE]"
git push
```


## Create new branch
```
git branch [BRANCH NAME]
```

## Check branches
```
git log --oneline --decorate
```

## Switch betwen branches
```
git checkout [BRANCH NAME]
```

## Advance check branchs
```
git log --oneline --decorate --graph --all
```

## Crate and switch to the branch
```
git checkout -b [BRANCH NAME]
```

---
---
---

# Python packages

> Note: use all command in the terminal

## Save all the packages you have
```
pip freeze > requirements.txt
```

## Install all packages that are in the requirements.txt
```
pip install -r requirements.txt
```

## Remove all the packages you have
```
pip freeze | xargs pip uninstall -y
```

## Remove pip
```
pip uninstall pip
```

## install pip
Use 
[this](https://pip.pypa.io/en/stable/installation/)
guide.