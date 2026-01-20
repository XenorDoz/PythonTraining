# Welcome !

## Welcome to Python !  

Python is a simple, readable programming language used almost everywhere — from small scripts to web apps, data science, automation, and even games.
It’s one of the easiest languages to learn, which makes it perfect for beginners.

## Before starting

Make sure everythin is installed and ready:
- [**Install python** ](../README.md#installing-python)
- [**Set up Python in  your IDE**](../README.md#setting-up-python-for-your-ide)

*Just in case, I've added extra tutorials in the [README.md](../README.md)*

## How to use the terminal

This is a quick tutorial on how to use the terminal.  
You can skip to [How to run a Python file](#how-to-run-a-python-file) if you already know !

First of all, you need to open a terminal :
- If your IDE has one, you can open it from the top menu or with a shortcut (for VS Code it's ```Ctrl + ` ```, for PyCharm it's `Alt + F12`)
- Otherwise, use your operating system's terminal (press the Windows key and type `cmd`)

To move between your folders, use `cd` followed by the folder name!  
*Small tip, a folder named `../` is hidden, it means "go back one folder"*
```bash
cd lessons 
cd ../
cd exercises/00_introduction
```

You can list everything that is in the current folder by using the `ls` command too !

## How to run a Python file

To execute a Python script, you need to: 
1. Open a **terminal**
2. Be in the **same folder** as your `.py` file
3. Run:
   ```bash
   python myFile.py
   ```

A few important notes :
- The file **must** end with `.py`
- The terminal's **current folder matters** 
- If Python is installed correctly, it should run without erros
- If nothing happens, check that you typed the command right

This is the basic workflow you'll use to run any script.

## Time to test !

Every exercise will be in the folder corresponding the lesson.  
As an example, this lesson is named `00_introduction` in the folder `lessons`, so the corresponding exercises are in `exercises/00_introduction`.  

In this folder, you'll find:
- The initial script given
- A file `input.md` with some data you can test your script with
- A file `output.md` with what you should get when using the input file
  
If an `input.md` or `output.md` file is needed for the exercise, it will be mentioned.  
If it is not listed, then it is normal that the file does not exist in the folder.

There's a file ready to run in the [exercise folder](../exercises/) so you can check that everything works!

In your IDE, get into the folder [exercises/00_introduction](../exercises/00_introduction/), and open your terminal here.  
It should be written something like: 
```bash
..\PythonTraining\exercises\00_introduction>
```  
Then, try to run the file [exercise0.py](../exercises/00_introduction/exercise0.py) !  
Your terminal should display the same result as the `output.md` file in the corresponding directory.