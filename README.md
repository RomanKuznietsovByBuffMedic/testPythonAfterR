# How use Git and GitHub

Just make step-by-step from 
[this](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/)
tutorial.

## Notes

> **Name repo**: the  name of the repository from GitHub will be the name of the folder with the project on the local machine.

**Example**: 

```
`[GITHUB NAME] / MyRepository` => `[PATH TO FOLDER]/MyRepository` 
```

---

> **Path repo**: in the terminal before `git clone [HTTPS ADDRESS]` go to the folder where the folder from GitHub will be created.

**Example**: 

```
$ cd [PATH TO FOLDER]
$ git clone [HTTPS ADDRESS]
```

This make project folder `[PATH TO FOLDER]/MyRepository`.

---

> **First push**: the first time you use `git push` use the branch that is shown in `git status`.

**Example**: 

```
$ git status
```
On branch **main**

some text
```
$ git push origin main
```
