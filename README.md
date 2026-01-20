# This is a training on python stuff

This git contains some exercises to help learning python, with one solution for each.  
You can either get the whole git so you get the base file and the correction, or just go to the exercises:

- [This is a training on python stuff](#this-is-a-training-on-python-stuff)
  - [How to get the files](#how-to-get-the-files)
    - [Get git](#get-git)
    - [How to use git](#how-to-use-git)
      - [Create a repo (optional)](#create-a-repo-optional)
      - [Save your work](#save-your-work)
      - [Upload your work](#upload-your-work)
      - [Get the latest updates](#get-the-latest-updates)
    - [Download everything](#download-everything)
  - [Installing python](#installing-python)
  - [Setting up Python for your IDE](#setting-up-python-for-your-ide)
    - [VS Code](#vs-code)
    - [PyCharm](#pycharm)
    - [Other IDEs](#other-ides)
  - [How to run Python](#how-to-run-python)
  - [Exercises](#exercises)

## How to get the files

To grab these files, you have two options :
- [Install git and use it to create your own repo](#get-git)
- [Download the .zip of everything](#download-everything)

### Get git

If you want to use Git (recommended but not necessary):

1. **Install Git** from the official website:  
    https://git-scm.com/downloads
2. **Open a terminal** in the folder you want (Command Prompt or your IDE terminal)  
   *As an example, if you want it to be in C:\Users\<user>\Code :*  
   *Move to that folder, then click on the link on top (would be something like `C: > Users > Xen > Code`)*  
   *And simply type cmd, this will open it at the right place*
3. **Clone the repository**:
   ```bash 
   git clone https://github.com/XenorDoz/PythonTraining.git
   ```
4. **Move** into the **projet folder**:   
   ```bash
   cd PythonTraining
   ```

And you have all the files !  
You can now continue to learn how to use git, skip to either [installing python](#installing-python) if you have not installed it, or go directly to the [exercises](#exercises) !
___
### How to use git
- [Create a repo (fully optional)](#create-a-repo)
- [Save your work](#save-your-work)
- [Upload your work (only if you have a repo)](#upload-your-work)
- [Get the latest updates](#get-the-latest-updates)

#### Create a repo (optional)
If you want to save your work online, you need your own GitHub repository:  
1. Sign in your GitHub account
2. Create a New Repository
3. Choose a name
4. Click Create Repository

GitHub will show you a line like:
```bash
git remote add origin https://github.com/<yourname>/<yourrepo>.git
```
Copy it and run it in your terminal, in the main folder with everything
*If you did it in something like `C: > Users > Xen > Code`, then your terminal should show `C:\Users\Xen\Code>`, you paste it here*
___

#### Save your work
To save your work, you first have to add everything you want to save:
```bash
git add <file>
```  
*Example : `git add myFile.py`*  
*Protip :  If you want to save everything in that folder, do `git add .`* 

Then, you have to send it to git with a message:  
```bash
git commit -m "message"
```  
*Something like `git commit -m "Added my function"`*
___

#### Upload your work
*This only works if you have your own repo*
To send it to GitHub and find your work on your online repo, simply do:
```bash
git push
```
And that's it, everything commited is now online!
___

#### Get the latest updates
If new stuff is added, do this:  
```bash
git fetch
git pull
```
If you already modified the exercises, Git may warn you that your files are different with a message like this:  
```bash
CONFLICT (content): Merge conflict in <filename>
Automatic merge failed
```
This is normal — it just means Git found differences between **your work** and the **updated version**.

**To keep your work safely:**
```bash
git add .
git commit -m "My progress"
git pull
```
**If there is a conflict**
Git will mark the conflicting parts inside the file like this:
```bash
<<<<<< HEAD
your version
=======
new version from the repo
>>>>>> origin/main
```
To fix it:
1. **Open** the file
2. **Choose** what you want to keep (usually your version)
3. **Delete** the conflict markers
4. **Save** the file
5. Tell Git you fixed it:
```bash
git add .
git commit -m "Solved merge conflict"
```
Your work is now preserved, and you also have the updated files.

### Download everything

If you don't want to use Git, no worries !

1. **Go** to the **GitHub page** of this repository 
2. **Click** on the **green Code button**
3. Select **Download ZIP**
4. **Extract** the ZIP file where you want
5. **Open** the folder in your editor

And you now have every file !  
If you need to install python, continue reading, otherwise head to the [exercises](#exercises) !

## Installing python

Here's how to install python on your pc:

1. **Download** it from the official website:  
   https://www.python.org/downloads/
2. During the installation, **check the box "Add Python to PATH"**
3. Once installed, **verify** it by running in a terminal:
   ```bash
   python --version
   ```
   If the version is shown, you're good!

## Setting up Python for your IDE

### VS Code

1. **Open** the project folder
2. Press **Ctrl + Shift + P**
3. Type **“Python: Select Interpreter”**
4. **Choose** the Python version you **installed** (for example: `Python 3.x.x`)
5. VS Code will now use this Python to run your scripts

### PyCharm
1. **Open** the project
2. Go to **File → Settings → Project → Python Interpreter**
3. Click the gear icon → **Add Interpreter**
4. Choose **System Interpreter**
5. Select the Python executable (usually in `C:\Users\<you>\AppData\Local\Programs\Python\Python3x\python.exe`)
6. Validate
   
### Other IDEs
Most IDEs have a setting called **Interpreter**, **Python Path**, **or Python Executable**.
Just select the Python you installed earlier.

## How to run Python
To run any file, open a terminal in the folder and type:
```bash
python myFile.py
```
*If you want to run exercise4.py, do `python exercise4.py`*

## Exercises