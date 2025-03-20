# How use Git and GitHub

Just make step-by-step from [this](https://www.freecodecamp.org/news/a-beginners-guide-to-git-how-to-create-your-first-github-project-c3ff53f56861/) tutorial

### Notes

> **Note about name repo**: the name of the repository from GitHub will be the name of the folder with the project on the local machine.

**Example**: 

```
`[GITHUB NAME] / MyRepository` => `[PATH TO FOLDER]/MyRepository` 
```

---

> **Note about repo path**: in the terminal before `git clone [HTTPS ADDRESS]` go to the folder where the folder from GitHub will be created

**Example**: 

```
$ cd [PATH TO FOLDER]
$ git clone [HTTPS ADDRESS]
```

This make folder `[PATH TO FOLDER]/MyRepository`
with project --- `MyRepository`

---

> **Note about first push**: the first time you use `git push` use the branch that is shown in `git status`

**Example**: 

```
$ git status
```
On branch **main**
some text
```
$ git push origin main
```


1. назва репозиторію з ГітХаба і буде назвою папки з проєктом на локальній машині
2. в терміналі перед `git clone [HTTPS ADDRESS]` зайди в теку, в якій створиться тека з GitHub'а 
3. вперше використовуючи `git push` використовуй гілку, яка показується в `git status`

